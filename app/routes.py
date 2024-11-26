from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
import socketio
from werkzeug.utils import secure_filename
from flask_login import current_user, login_user, login_manager, login_required
from app.models import Item, User, Notification
from app.forms import Registration, Login, Items, SearchItem
from flask_socketio import emit, join_room, leave_room
from app import db, app, socket
import email_validator
import os
import base64


sio = socketio.Server()

@app.route('/')
def loading():
    return render_template('loading.html')

@app.route('/index')
def first():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_pass(tryed_password=form.password.data):
            login_user(user)
            flash(f'Login efetuado com sucesso!', 'success' )
            return redirect(url_for('home_page', form=form))
        else:
            flash('Email ou senha incorretos', category='danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = Registration()
    if form.validate_on_submit():
        user_to_create = User(name=form.username.data,
                              email =form.email.data,
                              phone_number=form.phone_number.data,
                              password=form.password1.data)   
        db.session.add(user_to_create)
        db.session.commit()    
        return redirect(url_for('login_page', form=form))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Teve um erro com a criação de úsuario: {err_msg}') 
    
    return render_template('register.html', form=form)

@app.route('/home')     
@login_required
def home_page():
    categories = ['Automovel', 'Cosmeticos', 'Jogos', 'Telemovel', 'Computador', 'Vestes', 'Livros', 'Eletronicos', 'Outros']
    products = Item.query.order_by(Item.post_date.desc()).all()

    grouped_products = {}
    for category in categories:
        grouped_products = {category: [p for p in products if p.category == category] for category in categories}
    return render_template('home.html', products=products, grouped_products=grouped_products)

@app.route('/vender', methods=['POST', 'GET'])
@login_required
def sell_page():
    form = Items()
    if form.validate_on_submit():
       item_to_create = Item(name=form.name.data, price=form.price.data, category=form.category.data, description=form.description.data, seller_id=current_user.id)
       image = form.image.data
       item_to_create.image = image.read()    
       try:
        db.session.add(item_to_create)
        db.session.commit()
        print("Produto salvo com sucesso!")
        flash('Produto vendido com sucesso!')
        return redirect(url_for('home_page'), form=form)
       except Exception as e:
        flash(f"Erro ao salvar produto: {e}")
        return redirect(request.url) 
    if form.errors:
        for err_msg in form.errors.values():
            flash(f'Teve um erro com a criação e venda do produto: {err_msg}')

    return render_template('sell.html', form=form)

@app.template_filter('to_base64')
def to_base64(binary_data):
    return base64.b64encode(binary_data).decode('utf-8')

@app.route('/loja')
@login_required
def product_page():
    form = Items()
    category = request.args.get('category')

    if category == False:
        products = Item.query.order_by(Item.post_date.desc()).all()
    else:
        products = Item.query.filter_by(category=category).order_by(Item.post_date.desc()).all()

    return render_template('market.html', form=form, products=products)

@app.route('/produto/<int:id>')
def products_page(id):
    item = Item.query.get_or_404(id)
    return render_template('product.html', item=item)


@app.route('/perfil/<int:id>')
def profile_page(id):
    user = User.query.get_or_404(id)
    return render_template('partials/profile.html', user=user)

@app.route('/notificação')
def notification():
    notifi = Notification.query.order_by(Notification.message_date.desc()).all()
    return render_template('partials/notification.html', notifi=notifi)

@app.route('/meus-produtos')
def my_product():
    user_id = current_user.id
    products = Item.query.filter_by(seller_id=user_id).all()
    return render_template('partials/my_products.html', products=products)  

@app.route('/produtos-gostados')
def liked_products():
    return render_template('partials/liked.html')

@app.route('/produto/<int:id>')
def product(id):
    product = Item.query.get_or_404(id)
    return render_template('product.html', product=product)

@app.route('/notificando/<int:id>')
def notify(id):
    product = Item.query.get_or_404(id)
    notification = Notification(
        message=f'{current_user.name} achou seu produto interessante: {product.name}.',
        user_id=product.seller_id
    )
    db.session.add(notification)
    db.session.commit()
    sio.emit('notification', {'message': f'{current_user.name} achou seu produto interessante: {product.name}.'}, room=str(product.seller_id))
    flash('Adicionado aos produtos gostados!')
    return redirect(url_for('home_page', id=id))

@sio.event
def join(sid, data):
    user_id = data['user_id']
    sio.enter_room(sid, user_id)
    print(f'User {user_id} joined room {user_id}')

@sio.event
def leave(sid, data):
    user_id = data['user_id']
    sio.leave_room(sid, user_id)
    print(f'User {user_id} left room {user_id}') 


@app.route('/logout')
@login_required
def logout():
    print('Você foi desconectado!')
    return redirect(url_for('login_page'))


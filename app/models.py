from app import db, login_manager  
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    phone_number = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship('Item', backref='seller', lazy=True)
    notification = db.relationship('Notification', backref='user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = generate_password_hash(plain_text_password)

    def check_pass(self, tryed_password):
        return check_password_hash(self.password_hash, tryed_password)
        

    def __repr__(self):
        return f'User {self.name}, {self.email}, {self.phone_number}'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String)
    description = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime, default=datetime.utcnow)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    def __repr__(self):
        return f'Item {self.name}, {self.price}'

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    message_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
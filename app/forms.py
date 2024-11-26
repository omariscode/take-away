from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, EmailField, DecimalField, FileField, TextAreaField, TelField, SelectField, SearchField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from flask_wtf.file import FileAllowed
from app.models import User
import email_validator

class Registration(FlaskForm):
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("Este Email já existe! Por favor tente um diferente")
        

    username = StringField(label='Seu nome:', validators=[Length(min=2, max=30), DataRequired()])
    email = EmailField(label='Seu Email: ', validators=[DataRequired(), Email()])
    phone_number = TelField(label='Seu numero de telefone:', validators=[DataRequired()])
    password1 = PasswordField(label='Senha:', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirma a Senha:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Criar Conta')



class Login(FlaskForm):
    email = EmailField(label='Seu Email: ', validators=[DataRequired(), Email()])
    password = PasswordField(label='Senha:', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')

class Items(FlaskForm):
    name = StringField(label='Nome do produto:', validators=[DataRequired()])
    image = FileField(label='Imagem do produto:', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'heic', 'heif'])]) 
    price = DecimalField(label='Preço:', validators=[DataRequired()], places=2)  
    category = SelectField(label='Categoria de produto:',choices=[('Automovel','Automovel'),('Cosmeticos', 'Cosmeticos'), ('Jogos', 'Jogos'), ('Telemovel', 'Telemovel'), ('Computador', 'Computador'), ('Vestes', 'Vestuario'), ('Livros', 'Livro'), ('Eletronicos', 'Componentes eletricos'), ('Outros', 'Outros')] ,validators=[DataRequired(),])
    description = TextAreaField(label='Descrição do produto:', validators=[DataRequired()])
    submit = SubmitField(label='Vender')

class SearchItem(FlaskForm):
    search = SearchField(label='', validators=[DataRequired()])
    submit = SubmitField(label='Pesquisar')
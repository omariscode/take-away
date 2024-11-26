from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
import os
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'shdjgdfnklhfd'
app.config['WTF_CSRF_ENABLED'] = True
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
bcrypt = Bcrypt(app)
socket = SocketIO(app)

db = SQLAlchemy(app)

from app import routes

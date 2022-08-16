from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://uufzylpvhjkirs:c415913666e736e75dd1203b53533ad89897b7179968035b156691bee771b64b@ec2-44-195-100-240.compute-1.amazonaws.com:5432/d62mapd7sqku08"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '9203193009476448d996ce6d'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

login_manager = LoginManager()
db = SQLAlchemy()
csrf = CSRFProtect()
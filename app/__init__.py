from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'dev-fallback-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app import extensions as ext
    ext.db.init_app(app)
    # ext.login_manager.init_app(app)
    ext.csrf.init_app(app)

    from app.routes import main, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    return app


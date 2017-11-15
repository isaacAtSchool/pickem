# app/__init__.py

# third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

# login manager initialization
login_manager = LoginManager()

# initializes the flask app main object
def create_app(config_name):
    # app has an app object. Initialize app object
    app = Flask(__name__, instance_relative_config=True)
    # reads the config type pointed to by 'config_name' in 'app_config' dict
    app.config.from_object(app_config[config_name])
    # reads the config file in the instance folder
    app.config.from_pyfile('config.py')

    # flask component: database manager
    db.init_app(app)

    # placeholder / page for webpage
#    @app.route('/')
#    def hello_world():
#        return 'hello, World'
#
    # flask component: login manager
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"

    # flask component: migration tool - pushes changes in db model to mysql db
    migrate = Migrate(app, db)

    # flask component: boostrap tool - link WTForms to templates, other utils
    Bootstrap(app)

    from app import models

    # explicit relative import. the name of the module is the name of the folder
    # import the admin object from inside the admin module
    # relative imports occurs when you do imports within a package (app)
    # explicit imports (i think) would work here as well
    # i.e. from app.admin import admin
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app

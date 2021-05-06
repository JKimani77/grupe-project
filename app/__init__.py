from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_github import GitHub
###
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
###
mail = Mail()


#create login manager instance 
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def make_app(config_name):
    app = Flask(__name__,instance_relative_config = True)
    app.config['GITHUB_CLIENT_ID'] = 'XXX'
    app.config['GITHUB_CLIENT_SECRET'] = 'YYY'

    #For GitHub Enterprise
    app.config['GITHUB_BASE_URL'] = 'https://HOSTNAME/api/v3/'
    app.config['GITHUB_AUTH_URL'] = 'https://HOSTNAME/login/oauth/'

    #creating app configs
    app.config.from_object(config_options[config_name])

    #flask extnsions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    github.init_app(app)
    ###
    github = GitHub(app)

    # Registering the blueprints
    

    # setting config
    ###from .request import configure_request
    ###configure_request(app)

    return app
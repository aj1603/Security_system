from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from main.config import Config
from flask_migrate import Migrate
from flask_babel import Babel, format_date, gettext
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
babel = Babel(app)
login_manager = LoginManager(app)
login_manager.login_view = 'boss_login'
login_manager.login_message = 'Oýun ulgamyna giriň!'
login_manager.login_message_category = 'info'

from . import models

from main.security.routes import security
from main.admin.routes import admins
# from main.games.routes import ps4_ps5
from main.main_ui.routes import main_ui
from main.client.routes import clients
from main.games.routes import games

# app.register_blueprint(ps4_ps5)
app.register_blueprint(admins)
app.register_blueprint(security)
app.register_blueprint(main_ui)
app.register_blueprint(clients)
app.register_blueprint(games)



@babel.localeselector
def get_locale():
    language = Config.BABEL_DEFAULT_LOCALE
    if 'language' in session:
        language = session['language'] if session['language'] else Config.BABEL_DEFAULT_LOCALE
    return language

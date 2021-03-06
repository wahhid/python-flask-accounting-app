from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension
from flask_oauthlib.client import OAuth
from .config import Config

config = Config()


login_manager = LoginManager()
csrf = CSRFProtect()
db = MongoEngine()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.get_login'
login_manager.login_message = 'Please LOG IN'
login_manager.login_message_category = 'info'
toolbar = DebugToolbarExtension()
oauth = OAuth()

facebook = oauth.remote_app(
    'facebook',
    consumer_key=config.FACEBOOK_APP_ID,
    consumer_secret=config.FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    access_token_method='GET',
    authorize_url='https://www.facebook.com/dialog/oauth'
)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import plaid
from plaid.api import plaid_api
from dotenv import load_dotenv
from .config import Config

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # Initialize Plaid Client with the updated method
    configuration = plaid.Configuration(
      host=plaid.Environment.Sandbox,  # or plaid.Environment.Development/Production as needed
      api_key={
        'clientId': app.config['PLAID_CLIENT_ID'],
        'secret': app.config['PLAID_SECRET'],
        'plaidVersion': '2020-09-14'  # Make sure this version is still supported
      }
    )

    api_client = plaid.ApiClient(configuration)
    app.plaid_client = plaid_api.PlaidApi(api_client)

    # Register Blueprints
    # from .yourmodule import your_blueprint
    # app.register_blueprint(your_blueprint, url_prefix='/api/v1')

    # Error Handlers Below

    return app

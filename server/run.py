import os

from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager

from server.routes.auth_api import auth_bp
from server.routes.manage_api import manage_bp
from server.routes.trade_api import trade_bp
from server.routes.views import views

load_dotenv()


def _env_bool(name: str, default: bool) -> bool:
    v = os.getenv(name)
    if v is None:
        return default
    return v.strip().lower() in ("1", "true", "yes", "on")


def create_app():
    app = Flask(__name__, template_folder="./static")

    _loc = os.getenv("JWT_TOKEN_LOCATION", "headers")
    token_locations = [x.strip() for x in _loc.split(",") if x.strip()]

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret-key")
    app.config["JWT_TOKEN_LOCATION"] = token_locations or ["headers"]
    app.config["JWT_HEADER_TYPE"] = os.getenv("JWT_HEADER_TYPE", "Bearer")
    app.config["JWT_COOKIE_CSRF_PROTECT"] = _env_bool("JWT_COOKIE_CSRF_PROTECT", False)
    app.config["JWT_IDENTITY_CLAIM"] = os.getenv("JWT_IDENTITY_CLAIM", "identity")

    JWTManager(app)

    app.register_blueprint(views)
    app.register_blueprint(auth_bp)
    app.register_blueprint(trade_bp)
    app.register_blueprint(manage_bp)

    return app

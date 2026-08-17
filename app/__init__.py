from flask import Flask
from .config import Config
from .extensions import db, csrf

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # load the configuration
    app.config.from_object(config_class)
    
    # Initialize the extensions
    db.init_app(app)
    csrf.init_app(app)
    
    # register blueprints
    from .main.routes import main_bp
    from .auth.routes import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    return app
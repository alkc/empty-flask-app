"""Initialize Flask app."""
from flask import Flask

import config

def create_app() -> Flask:
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # Allows cross-origin requests for CDM/api
    # /trends needs this to work.
    # from flask_cors import CORS
    # CORS(app)

    app.logger.info("Loading config.DefaultConfig")
    app.config.from_object(config.DefaultConfig()) 
 
    if app.debug:
        app.logger.info("Loading config.DevelopmentConfig")
        app.config.from_object(config.DevelopmentConfig())
        
    with app.app_context():
        app.logger.info("Initializing app extensions.")
        # init_login_manager(app)
        # init_mongodb(app)
        register_blueprints(app)
        app.logger.info("Finished initializing app extensions.")
        
    app.logger.info("App initialization finished. Returning app.")
    return app


def init_mongodb(app) -> None:
    """
    Initialize pymongo.MongoClient extension
    """
    app.logger.info("Initializing mongodb at: "
                    f"{app.config['MONGO_URI']}")
    from app.extensions import mongo
    mongo.init_app(app)
  

def register_blueprints(app) -> None:
    
    app.logger.info("Initializing blueprints")

    def bp_debug_msg(msg):
        app.logger.debug(f'Blueprint added: {msg}')

    # Example Main:
    bp_debug_msg("cdm/main/views.py => home_bp")
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)

    
def init_login_manager(app) -> None:
    from cdm.extensions import login_manager
    app.logger.info("Initializing login_manager")
    login_manager.init_app(app)
    login_manager.login_view = "login_bp.login"

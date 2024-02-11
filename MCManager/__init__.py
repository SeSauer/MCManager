import os
from flask import Flask
from MCManager.backend import Manager

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    Manager.init(app.instance_path)

    #register Blueprints
    from .frontend.landing import bp as landing_bp
    app.register_blueprint(landing_bp)
    from .frontend.overview import bp as overview_bp
    app.register_blueprint(overview_bp)
    from .frontend.server_page import bp as server_bp
    app.register_blueprint(server_bp)


    return app
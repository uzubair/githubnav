""" Application module """
from flask import Flask
from flask.globals import current_app
from flask_bootstrap import Bootstrap
from .containers import Container
from . import views
import os


def create_app() -> Flask:
    config_file = os.path.join(".", "src", "backend", "config.yml")
    container = Container()
    container.config.from_yaml(config_file)
    container.wire(modules=[views])

    app = Flask(__name__)
    app.container = container
    app.add_url_rule("/", "index", views.index)

    bootstrap = Bootstrap()
    bootstrap.init_app(app)
    return app

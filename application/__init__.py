# -*- coding: utf-8 -*-
from flask import Flask
from application.apps.page.views import bp as page_view
from application.apps.api.views import bp as api_view
from application.dbms.rdb import db


def create_app(config=None):
    """ Application Factories
        http://flask.pocoo.org/docs/patterns/appfactories/
    """
    app = Flask(
        __name__, static_folder='static/dist', static_url_path='/static')
    if config:
        app.config.from_pyfile(config)
    else:
        app.config.from_envvar('APP_SETTINGS')

    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
    app.register_blueprint(api_view)
    app.register_blueprint(page_view)
    db.init_app(app)

    return app

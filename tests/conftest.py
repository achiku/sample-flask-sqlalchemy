# -*- coding: utf-8 -*-
import inspect

import pytest

from application import create_app
from application.dbms.rdb import db as _db

from . import factories


@pytest.yield_fixture(scope='session')
def app():
    app = create_app('../configs/local_test_postgres.py')
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.yield_fixture(scope='function')
def db(app):
    _db.drop_all()
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.yield_fixture(scope='function')
def session(db):
    # connect to the database
    connection = db.engine.connect()
    # begin a non-ORM transaction
    transaction = connection.begin()

    # bind an individual session to the connection
    # options = dict(bind=connection, binds={})
    options = dict(bind=connection)
    session = db.create_scoped_session(options=options)

    # overload the default session with the session above
    db.session = session

    # overload session in factory classes
    for name, cls in inspect.getmembers(factories, inspect.isclass):
        if cls.__class__.__name__ == 'FactoryMetaClass':
            cls._meta.sqlalchemy_session = session

    yield session
    session.close()
    # rollback - everything that happened with the
    # session above (including calls to commit())
    # is rolled back.
    transaction.rollback()
    # return connection to the Engine
    connection.close()


@pytest.fixture()
def test_client(app):
    return app.test_client()


@pytest.fixture()
def item_data(session):
    return factories.ItemFactory.create_batch(10)


@pytest.fixture()
def item_history_data(session):
    return factories.ItemHistoryFactory.create_batch(10)


@pytest.fixture()
def api_url_data(session):
    items = factories.ItemFactory.create_batch(2)
    return {
        'items': items,
        'single_item_id': items[0].id
    }

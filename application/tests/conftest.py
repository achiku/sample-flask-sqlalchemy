# -*- coding: utf-8 -*-
import pytest
from application import create_app
from ..dbms.rdb import db as _db
from .factories import (
    ItemFactory, ItemHistoryFactory,
)


@pytest.yield_fixture(scope='session')
def app():
    app = create_app('../configs/local_test_postgres.py')
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.yield_fixture(scope='session')
def db(app):
    _db.drop_all()
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.yield_fixture(scope='function')
def session(db):
    yield db.session
    db.session.flush()
    db.session.rollback()
    db.session.remove()


@pytest.fixture()
def test_client(app):
    return app.test_client()


@pytest.fixture()
def item_data(session):
    return ItemFactory.create_batch(10)


@pytest.fixture()
def item_history_data(session):
    return ItemHistoryFactory.create_batch(10)


@pytest.fixture()
def api_url_data(session):
    items = ItemFactory.create_batch(2)
    return {
        'items': items,
        'single_item_id': items[0].id
    }

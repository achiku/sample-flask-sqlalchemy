# -*- coding: utf-8 -*-
from flask.ext.script import Manager, prompt_bool
from application import db
from ..tests.factories import ItemFactory, ItemHistoryFactory
from ..dbms.large_models import ItemHistory
from ..dbms.small_models import Item


manager = Manager(usage="Perform database operations")


@manager.option('-d', '--dbname', dest='db_name', required=True)
def drop(db_name):
    "Drops database tables"
    if db_name == 'small':
        if prompt_bool("Are you sure you want to lose all your data"):
            db.drop_all(bind=None)
    elif db_name == 'large':
        if prompt_bool("Are you sure you want to lose all your data"):
            db.drop_all(bind='large_db')
    else:
        print "No DB named {}.".format(db_name)
    print "Done"


@manager.option('-d', '--dbname', dest='db_name', required=True)
def create(db_name):
    "Creates database tables from sqlalchemy models"
    if db_name == 'small':
        db.create_all(bind=None)
    elif db_name == 'large':
        db.create_all(bind='large_db')
    else:
        print "No DB named {}.".format(db_name)
    print "Done"


@manager.command
def populate():
    "Populate tables with dummy data"
    items = ItemFactory.create_batch(10)
    for i in items:
        ItemHistoryFactory.create(name=i.name)
    db.session.commit()
    print "Done"


@manager.command
def delete_data():
    "Delete all data"
    items = db.session.query(Item).all()
    item_histories = db.session.query(ItemHistory).all()
    for item in items:
        db.session.delete(item)
    for hist in item_histories:
        db.session.delete(hist)
    db.session.commit()
    print "Done"

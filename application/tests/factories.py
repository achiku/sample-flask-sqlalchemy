# -*- coding: utf-8 -*-
from datetime import datetime
import factory
from faker import Factory as FakeFactory
from factory.alchemy import SQLAlchemyModelFactory
from application.dbms.rdb import db
from application.dbms.large_models import ItemHistory
from application.dbms.small_models import Item


faker = FakeFactory.create()


class ItemFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Item
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda x: x)
    name = factory.Sequence(lambda x: 'item{}'.format(x))
    price = factory.LazyAttribute(
        lambda x: faker.random_element(elements=(100, 200, 300, 400)))


class ItemHistoryFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ItemHistory
        sqlalchemy_session = db.session

    recorded_at = datetime.now()
    name = factory.Sequence(lambda x: 'item{}'.format(x))
    price = factory.LazyAttribute(
        lambda x: faker.random_element(elements=(100, 200, 300, 400)))

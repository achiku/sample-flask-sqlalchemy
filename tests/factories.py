# -*- coding: utf-8 -*-
import datetime

import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Factory as FakeFactory

from application.dbms import large_models, small_models
from application.dbms.rdb import db

faker = FakeFactory.create()


class ItemFactory(SQLAlchemyModelFactory):

    id = factory.Sequence(lambda x: x)
    name = factory.Sequence(lambda x: 'item{}'.format(x))
    price = factory.LazyAttribute(
        lambda x: faker.random_element(elements=(100, 200, 300, 400)))

    class Meta:
        model = small_models.Item
        sqlalchemy_session = db.session


class ItemHistoryFactory(SQLAlchemyModelFactory):
    recorded_at = datetime.datetime.now()
    name = factory.Sequence(lambda x: 'item{}'.format(x))
    price = factory.LazyAttribute(
        lambda x: faker.random_element(elements=(100, 200, 300, 400)))

    class Meta:
        model = large_models.ItemHistory
        sqlalchemy_session = db.session

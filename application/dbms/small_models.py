# -*- coding: utf-8 -*-
from .rdb import db


class Item(db.Model):
    """ Item """

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return u"<Item:({}, {})>".format(self.id, self.name)

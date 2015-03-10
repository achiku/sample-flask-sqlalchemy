# -*- coding: utf-8 -*-
from .rdb import db


class ItemHistory(db.Model):
    """ Item """

    __bind_key__ = 'large_db'
    __tablename__ = 'item_history'

    recorded_at = db.Column(db.DateTime, primary_key=True)
    name = db.Column(db.String, primary_key=True)
    price = db.Column(db.Integer)

    def __repr__(self):
        return u"<ItemHistory:({}, {})>".format(self.recorded_at, self.name)

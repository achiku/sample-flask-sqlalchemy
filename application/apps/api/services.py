# -*- coding: utf-8 -*-
from ...dbms.large_models import ItemHistory
from ...dbms.small_models import Item
from ...dbms.rdb import db
from ...libs.utils import sqla2dict, kt2dict


def get_items():
    items = db.session.query(Item)
    return [sqla2dict(i) for i in items]


def get_item(item_id):
    item = db.session.query(Item).get(item_id)
    return sqla2dict(item)


def get_item_history():
    items = db.session.query(ItemHistory)
    return [sqla2dict(i) for i in items]

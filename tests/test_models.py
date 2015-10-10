# -*- coding: utf-8 -*-
from application.dbms.large_models import ItemHistory
from application.dbms.small_models import Item


def test_item_model(item_data):
    items = Item.query.all()
    assert len(items) == len(item_data)


def test_item_history_model(item_history_data):
    histories = ItemHistory.query.all()
    assert len(histories) == len(item_history_data)

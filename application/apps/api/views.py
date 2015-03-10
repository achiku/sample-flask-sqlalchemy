# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from .services import (
    get_items, get_item, get_item_history,
)

bp = Blueprint(
    'api', __name__, url_prefix='/api')


@bp.route('/items/<int:item_id>/', methods=['GET'])
def item(item_id):
    result = get_item(item_id)
    return jsonify({'result': result})


@bp.route('/items/', methods=['GET'])
def items():
    result = get_items()
    return jsonify({'result': result})


@bp.route('/items/history/', methods=['GET'])
def item_history():
    result = get_item_history()
    return jsonify({'result': result})

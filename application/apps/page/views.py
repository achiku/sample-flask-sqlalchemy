# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint(
    'page', __name__, url_prefix='',
    template_folder='templates')


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.jade')


@bp.route('/items/', methods=['GET'])
def items():
    return render_template('items.jade')


@bp.route('/items/<int:item_id>/', methods=['GET'])
def item(item_id):
    return render_template('item.jade')

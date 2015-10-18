# -*- coding: utf-8 -*-
from configs.common import *  # NOQA

# built-in constraints
DEBUG = True
SECRET_KEY = 'r7ptv$112bm1ybx1ksw$tlxf7f31s1'

SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
SQLALCHEMY_BINDS = {
        'large_db': 'sqlite://:memory:'
}

try:
    from configs.local import *  # NOQA
except ImportError:
    pass

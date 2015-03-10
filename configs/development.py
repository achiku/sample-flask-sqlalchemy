# -*- coding: utf-8 -*-
from configs.common import *  # NOQA

# built-in constraints
DEBUG = True
SECRET_KEY = 'r7ptv$112bm1ybx1ksw$tlxf7f31s1'

SQLALCHEMY_DATABASE_URI = 'postgresql://app:dev@localhost/db1'
SQLALCHEMY_BINDS = {
    'large_db': 'postgresql://app:dev@localhost/db2'
}

try:
    from configs.local import *  # NOQA
except ImportError:
    pass

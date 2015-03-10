# -*- coding: utf-8 -*-


def kt2dict(keyed_tuple):
    """ sqlalchemy.util._collections.KeyedTuple to dict """
    return dict(zip(keyed_tuple.keys(), keyed_tuple))


def sqla2dict(model):
    """ Declarative Base model to dict """
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

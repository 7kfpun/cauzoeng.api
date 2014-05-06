# -*- coding: utf-8 -*-
from ccy import currencydb
from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb
import logging


logger = logging.getLogger(__name__)


class User(EndpointsModel):
    """ User models."""

    _message_fields_schema = ('mac', 'created_date')

    mac = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
    address = ndb.StringProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)


class Item(EndpointsModel):
    """ Item models."""

    _message_fields_schema = (
        'id', 'user', 'title', 'price', 'currency', 'description',
        'second_hand', 'condition',
        'created_date', 'available_days', 'phone', 'email', 'location'
    )

    user = ndb.StringProperty(required=True)  # mac
    #user = ndb.KeyProperty(kind=User)

    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty(required=True)
    currency = ndb.StringProperty(required=True, choices=currencydb().keys())
    description = ndb.StringProperty(required=True)
    second_hand = ndb.BooleanProperty(required=True)
    condition = ndb.StringProperty(choices=[
        'VERY_OLD', 'OLD', 'NORMAL', 'NEW', 'VERY_NEW'])
    img = ndb.StringProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    available_days = ndb.IntegerProperty(required=True)

    phone = ndb.StringProperty()
    email = ndb.StringProperty()
    location = ndb.GeoPtProperty()

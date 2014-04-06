# -*- coding: utf-8 -*-
from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb


class User(EndpointsModel):
    """ User models."""

    #_message_fields_schema = ('id', 'name', 'phone', 'address')

    mac = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    #surname = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    address = ndb.StringProperty(required=True)


class Lottery(EndpointsModel):
    """ Lottery models."""

    _message_fields_schema = (
        'id', 'subject', 'price', 'description', 'url', 'created',
        'finish_date', 'user')

    subject = ndb.StringProperty(required=True)
    price = ndb.FloatProperty(required=True)
    description = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)
    img = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    finish_date = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.StringProperty()


class Bet(EndpointsModel):
    """ Bet models."""

    _message_fields_schema = ('id', 'user', 'lottery', 'created')

    user = ndb.StringProperty(required=True)
    lottery = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

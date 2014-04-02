# -*- coding: utf-8 -*-
from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb


class Lottery(EndpointsModel):
    """ Lottery models."""

    _message_fields_schema = (
        'id', 'title', 'subject', 'description', 'url', 'created', 'finished')

    title = ndb.StringProperty()
    subject = ndb.StringProperty()
    description = ndb.StringProperty()
    url = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    finished = ndb.DateTimeProperty(auto_now=True)


class Bet(EndpointsModel):
    """ Bet models."""

    _message_fields_schema = ('id', 'user', 'lottery', 'created')

    user = ndb.StringProperty(required=True)
    lottery = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from protorpc import messages
from protorpc.message_types import DateTimeField


class Greeting(messages.Message):
    """Greeting that stores a message."""

    id = messages.IntegerField(1)
    message = messages.StringField(2)
    description = messages.StringField(3)
    subject = messages.StringField(4, default='MAMA')
    url = messages.StringField(5)
    created_date = DateTimeField(6)
    finish_date = DateTimeField(7)


class GreetingCollection(messages.Message):
    """Collection of Greetings."""
    items = messages.MessageField(Greeting, 1, repeated=True)


STORED_GREETINGS = GreetingCollection(items=[
    Greeting(
        id=0, message='hello world!',
        subject="lucky draw 1",
        description="this is the 1st lucky draw!",
        url='https://developers.google.com/appengine/docs/python/tools/protorpc/messages/fieldclass',  # noqa
        finish_date=datetime.now() + timedelta(days=14),
    ),
    Greeting(
        id=1, message='goodbye world!',
        subject="lucky draw 2",
        description="this is the 2nd lucky draw!",
        url='https://developers.google.com/appengine/docs/python/tools/uploadinganapp',  # noqa
        finish_date=datetime.now() + timedelta(days=24),
    ),
    Greeting(
        id=2, message='goodbye again world!',
        subject="lucky draw 3",
        description="this is the 3rd lucky draw!",
        url='https://developers.google.com/appengine/docs/python/',
        finish_date=datetime.now() + timedelta(days=34),
    ),
    Greeting(
        id=3, message='goodbye again world!',
        subject="lucky draw 4",
        description="this is the 3rd lucky draw!",
        url='https://developers.google.com/appengine/docs/python/',
        finish_date=datetime.now() + timedelta(days=34),
    ),
    Greeting(
        id=4, message='goodbye again world!',
        subject="lucky draw 5",
        description="this is the 3rd lucky draw!",
        url='https://developers.google.com/appengine/docs/python/',
        finish_date=datetime.now() + timedelta(days=34),
    ),
    Greeting(
        id=5, message='goodbye again world!',
        subject="lucky draw 6",
        description="this is the 3rd lucky draw!",
        url='https://developers.google.com/appengine/docs/python/',
        finish_date=datetime.now() + timedelta(days=34),
    ),
    Greeting(
        id=6, message='goodbye again world!',
        subject="lucky draw 7",
        description="this is the 3rd lucky draw!",
        url='https://developers.google.com/appengine/docs/python/',
        finish_date=datetime.now() + timedelta(days=34),
    ),
])

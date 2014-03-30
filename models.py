# -*- coding: utf-8 -*-
from protorpc import messages
from protorpc.message_types import DateTimeField


class Greeting(messages.Message):
    """Greeting that stores a message."""

    message = messages.StringField(1)
    description = messages.StringField(2)
    subject = messages.StringField(3, default='MAMA')
    url = messages.StringField(4)
    finish_date = DateTimeField(5)


class GreetingCollection(messages.Message):
    """Collection of Greetings."""
    items = messages.MessageField(Greeting, 1, repeated=True)

# -*- coding: utf-8 -*-
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models import Greeting, GreetingCollection


package = 'Hello'


STORED_GREETINGS = GreetingCollection(items=[
    Greeting(message='hello world!', subject="HAHA",
             description="this is the 1st lucky draw!"),
    Greeting(message='goodbye world!', subject="HAHA",
             description="this is the 2nd lucky draw!"),
    Greeting(message='goodbye again world!', subject="WAWA",
             description="this is the 3rd lucky draw!"),
])


@endpoints.api(name='helloworld', version='v1')
class HelloWorldApi(remote.Service):
    """Helloworld API v1."""

    @endpoints.method(message_types.VoidMessage, GreetingCollection,
                      path='hellogreeting', http_method='GET',
                      name='greetings.listGreeting')
    def greetings_list(self, unused_request):
        return STORED_GREETINGS

    ID_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        id=messages.IntegerField(1, variant=messages.Variant.INT32))

    @endpoints.method(ID_RESOURCE, Greeting,
                      path='hellogreeting/{id}', http_method='GET',
                      name='greetings.getGreeting')
    def greeting_get(self, request):
        try:
            return STORED_GREETINGS.items[request.id]
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Greeting %s not found.' %
                                              (request.id,))

    MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(
        Greeting,
        times=messages.IntegerField(2, variant=messages.Variant.INT32,
                                    required=True))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE, Greeting,
                      path='hellogreeting/{times}', http_method='POST',
                      name='greetings.multiply')
    def greetings_multiply(self, request):
        return Greeting(message=request.message * request.times)


APPLICATION = endpoints.api_server([HelloWorldApi])

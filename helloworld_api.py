# -*- coding: utf-8 -*-
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from models import Greeting, GreetingCollection, STORED_GREETINGS

from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


package = 'Hello'


class MyModel(EndpointsModel):
    attr1 = ndb.StringProperty()
    attr2 = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)


@endpoints.api(name='helloworld', version='v1', description='My Little API')
class MyApi(remote.Service):

    @MyModel.method(path='mymodel', http_method='POST', name='mymodel.insert')
    def MyModelInsert(self, my_model):
        my_model.put()
        return my_model

    @MyModel.query_method(path='mymodels', name='mymodel.list')
    def MyModelList(self, query):
        return query


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


APPLICATION = endpoints.api_server([MyApi])

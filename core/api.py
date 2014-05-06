# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.path.insert(0, 'libs')


#from datetime import datetime, timedelta
from protorpc import remote
from models import Item, User
import endpoints
import logging


logger = logging.getLogger(__name__)
package = 'cauzoeng'

QUERY_LIMIT = 50


@endpoints.api(name='core', version='v1', description='API')
class CoreApi(remote.Service):

    # User resource
    @User.method(path='user', http_method='POST', name='user.insert')
    def UserInsert(self, user):
        user.put()
        return user

    @User.method(request_fields=('id',),
                 path='user/{id}/', http_method='GET', name='user.get')
    def UserGet(self, user):

        if not user.from_datastore:
            raise endpoints.NotFoundException('Not found.')
        return user

    @User.query_method(
        query_fields=('limit', 'order', 'pageToken'),
        limit_default=QUERY_LIMIT,
        path='user', name='user.list')
        #collection_fields=('id', 'title', 'subject', 'description', 'url',
                           #'created', 'finished', 'user'),
    def UserList(self, query):
        logger.info(query)
        return query

    # Item resource
    @Item.method(path='item', http_method='POST', name='item.insert')
    def ItemInsert(self, item):
        item.put()
        return item

    @Item.method(request_fields=('id',),
                 path='item/{id}/', http_method='GET', name='item.get')
    def ItemGet(self, item):

        if not item.from_datastore:
            raise endpoints.NotFoundException('Not found.')
        return item

    @Item.query_method(
        query_fields=('limit', 'order', 'pageToken'),
        limit_default=QUERY_LIMIT,
        path='item', name='item.list')
        #collection_fields=('id', 'title', 'subject', 'description', 'url',
                           #'created', 'finished', 'item'),
    def ItemList(self, query):
        logger.info(query)
        return query

    #@Bet.method(path='bet', http_method='POST', name='bet.insert')
    #def BetInsert(self, bet):
        #logger.info(bet)
        #if not Lottery.get_by_id(long(bet.lottery)):
            #raise endpoints.NotFoundException('not found.')

        #last_bet = Bet.query(
            #Bet.user == bet.user, Bet.lottery == bet.lottery
        #).order(-Bet.created).get()
        #logger.info(last_bet)
        #if datetime.now() - last_bet.created < timedelta(hours=2):
            #logger.info(datetime.now() - last_bet.created)
            #raise endpoints.BadRequestException(
                #str((datetime.now() - last_bet.created).seconds))

        #bet.put()
        #return bet

    #@Bet.query_method(path='bet', name='bet.list')
    #def BetList(self, query):
        #return query

    #@User.method(path='user', http_method='POST', name='user.insert')
    #def UserInsert(self, user):
        #user.put()
        #return user


APPLICATION = endpoints.api_server([CoreApi])

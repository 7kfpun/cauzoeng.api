# -*- coding: utf-8 -*-
import endpoints
import logging
from datetime import datetime, timedelta
from protorpc import remote
from models import Bet, Lottery, User


logger = logging.getLogger(__name__)
package = 'cauzoeng'

QUERY_LIMIT = 50


@endpoints.api(name='lottery', version='v1', description='Lottery API')
class LotteryApi(remote.Service):

    @Lottery.method(path='lottery', http_method='POST', name='lottery.insert')
    def LotteryInsert(self, lottery):
        lottery.put()
        return lottery

    @Lottery.method(request_fields=('id',),
                    path='lottery/{id}', http_method='GET', name='lottery.get')
    def LotteryGet(self, lottery):

        if not lottery.from_datastore:
            raise endpoints.NotFoundException('Not found.')
        return lottery

    @Lottery.query_method(
        query_fields=('limit', 'order', 'pageToken'),
        limit_default=QUERY_LIMIT,
        path='lottery', name='lottery.list')
        #collection_fields=('id', 'title', 'subject', 'description', 'url',
                           #'created', 'finished', 'user'),
    def LotteryList(self, query):
        logger.info(query)
        return query

    @Bet.method(path='bet', http_method='POST', name='bet.insert')
    def BetInsert(self, bet):
        logger.info(bet)
        if not Lottery.get_by_id(long(bet.lottery)):
            raise endpoints.NotFoundException('not found.')

        last_bet = Bet.query(
            Bet.user == bet.user, Bet.lottery == bet.lottery
        ).order(-Bet.created).get()
        logger.info(last_bet)
        if datetime.now() - last_bet.created < timedelta(hours=2):
            logger.info(datetime.now() - last_bet.created)
            raise endpoints.BadRequestException(
                str((datetime.now() - last_bet.created).seconds))

        bet.put()
        return bet

    @Bet.query_method(path='bet', name='bet.list')
    def BetList(self, query):
        return query

    @User.method(path='user', http_method='POST', name='user.insert')
    def UserInsert(self, user):
        user.put()
        return user


APPLICATION = endpoints.api_server([LotteryApi])

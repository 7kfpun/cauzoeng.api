# -*- coding: utf-8 -*-
import endpoints
from protorpc import remote
from models import Bet, Lottery


package = 'cauzoeng'


@endpoints.api(name='lottery', version='v1', description='Lottery API')
class LotteryApi(remote.Service):

    @Lottery.method(path='lottery', http_method='POST', name='lottery.insert')
    def LotteryInsert(self, lottery):
        lottery.put()
        return lottery

    @Lottery.query_method(
        query_fields=('limit', 'order', 'pageToken'),
        path='lottery', name='lottery.list')
    def LotteryList(self, query):
        return query

    @Bet.method(path='bet', http_method='POST', name='bet.insert')
    def BetInsert(self, bet):
        bet.put()
        return bet

    @Bet.query_method(path='bet', name='bet.list')
    def BetList(self, query):
        return query


APPLICATION = endpoints.api_server([LotteryApi])

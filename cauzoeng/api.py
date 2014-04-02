# -*- coding: utf-8 -*-
import endpoints
from protorpc import remote
from models import Lottery


package = 'cauzoeng'


@endpoints.api(name='lottery', version='v1', description='Lottery API')
class LotteryApi(remote.Service):

    @Lottery.method(path='lottery', http_method='POST', name='lottery.insert')
    def LotteryInsert(self, lottery):
        lottery.put()
        return lottery

    @Lottery.query_method(path='lottery', name='lottery.list')
    def LotteryList(self, query):
        return query


APPLICATION = endpoints.api_server([LotteryApi])

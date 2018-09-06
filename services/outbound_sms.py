from datetime import datetime
from flask.views import MethodView

from base_sms_validation import BaseSMS


class OutboundSMS(MethodView, BaseSMS):
    def __init__(self):
        self.message = "outbound sms ok"
        pass

    def check_db(self, from_num):
        print "checking db"
        sql = "select number from account a join phone_number p on a.id=p.account_id where number=%s"%from_num
        res = self.cur.execute(sql)
        print "checked db"
        if res:
            return True
        else:
            raise Exception("from parameter not found")


    def check_cache(self, from_num):
        print "checking cache"
        from_num_data = self.get_cache(from_num)
        print from_num_data
        if from_num_data:
            count = from_num_data.get('count')
            if count >= 5:
                raise Exception("Limit reached for from %s"%from_num)
            initial_time = from_num_data.get('initial_time')
            if (datetime.now() - initial_time).days >= 1:
                self.store_cache(from_num, {'count':1, 'initial_time':datetime.now()}, 0)
            else:
                inc_count = count + 1
                self.store_cache(from_num, {'count': inc_count, 'initial_time': initial_time}, 0)
        else:
            self.store_cache(from_num, {'count': 1, 'initial_time': datetime.now()}, 0)
        print "checked cache"

    def check_from_data(self, from_num):
        self.check_db(from_num)
        self.check_cache(from_num)

    def process_data(self, data):
        from_num = data.get('from')
        to_num = data.get('to')
        if self.get_cache(self.from_to):
            raise Exception("sms from %s to %s blocked by STOP request"%(from_num,to_num))
        self.check_from_data(from_num)

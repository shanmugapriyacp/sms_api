import json
import pymysql

import validictory
from flask import request
from flask_restful import abort

from services.config import inboundsms_data
from services.custom_exceptions import UnAuthorizedException

from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()

class BaseSMS(object):
    def __init__(self):
        pass

    def __validate__(self, data):
        try:
            validictory.validate(data, inboundsms_data)
        except ValueError:
            raise

    def __authenticate__(self, username, password):
        db = pymysql.connect(host='localhost', port=3306, user='root', password='Shan@1616', db='user_contact')
        self.cur = db.cursor(pymysql.cursors.DictCursor)
        sql = "select username from account where username='%s' and auth_id=%s"%(username,password)
        res = self.cur.execute(sql)
        if res:
            return True
        else:
            raise UnAuthorizedException("Unauthorised user")

    def store_cache(self,key, value, timeout):
        cache.set(key,value,timeout=timeout)

    def get_cache(self,key):
        return cache.get(key)

    def post(self):
        try:
            print "In post"
            data = json.loads(request.data)
            self.__validate__(data)
            self.__authenticate__(data.get('username'), data.get('auth_id'))
            self.from_to = str(data.get('from')) + '_' + str(data.get('to'))
            self.process_data(data)
            return self.message
        except ValueError:
            raise
        except UnAuthorizedException:
            abort(403)
        except Exception as e:
            if e.message:
                message = e.message
            else:
                message = "Unknown failure"
            raise Exception(message)

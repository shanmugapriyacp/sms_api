from flask.views import MethodView

from base_sms_validation import BaseSMS


class InboundSMS(MethodView, BaseSMS):
    def __init__(self):
        self.message = "Inbound sms ok"

    def process_data(self,data):
        text = data.get('text')
        if text.startswith("STOP"):
            self.store_cache(self.from_to,True,4*60*60)
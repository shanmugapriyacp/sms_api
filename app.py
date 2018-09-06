from flask import Flask

from services.outbound_sms import OutboundSMS
from services.inbound_sms import InboundSMS


app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

app.add_url_rule(
    '/inbound/sms/',
    view_func=InboundSMS.as_view('inbound_sms'),
    methods=['POST'])

app.add_url_rule(
    '/outbound/sms/',
    view_func=OutboundSMS.as_view('outbound_sms'),
    methods=['POST'])
 
if __name__ == "__main__":
    app.run(debug=True)#,port=8000,host='192.168.56.102')

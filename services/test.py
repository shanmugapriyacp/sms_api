import requests
import json

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
ib_url = "http://127.0.0.1:5000/inbound/sms/"
post_data = {"username":"mark",
             "auth_id":1231,
             "from":9888888888,
             "to":9898989898,
             "text":"Hello"}
ib_response = requests.post(url=ib_url, data=json.dumps(post_data),headers=headers)
print ib_response.text

ob_url = "http://127.0.0.1:5000/outbound/sms/"
ob_response = requests.post(url=ob_url, data=json.dumps(post_data),headers=headers)

print ob_response.text

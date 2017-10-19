"""
일반매수
"""
import base64
import simplejson as json
import hashlib
import hmac
import httplib2
import time

ACCESS_KEY = ''
SECRET_KEY = ''
currency = 'btc-krw'

def get_encoded_payload(payload):
  dumped_json = json.dumps(payload)
  encoded_json = base64.b64encode(dumped_json)
  return encoded_json

def get_signature(encoded_payload, secret_key):
  signature = hmac.new(str(secret_key), str(encoded_payload), hashlib.sha512);
  return signature.hexdigest()

def get_response(url, payload):
  encoded_payload = get_encoded_payload(payload)
  headers = {
    'content-type': 'application/json',
    'X-COINRAIL-PAYLOAD': encoded_payload,
    'X-COINRAIL-SIGNATURE': get_signature(encoded_payload, SECRET_KEY)
  }
  http = httplib2.Http()
  response, content = http.request(url, 'POST', headers=headers, body=encoded_payload)
  return content

def limit_buy():
  url = 'https://api.coinrail.co.kr/order/limit/buy'
  payload = {
    "access_key": ACCESS_KEY,
    "currency": currency,
    "price" : 4900000,
    "qty" : 0.1,
    "timestamp" : int(round(time.time() * 1000))
  }

  response = get_response(url, payload)
  print response
  content = json.loads(response)

  return content

if __name__   == "__main__":
    print limit_buy()
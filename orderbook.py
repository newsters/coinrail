"""
오더북 조회
"""
import httplib2

url = 'https://api.coinrail.co.kr/public/orderbook'
currency = 'btc-krw'

if __name__   == "__main__":
  http = httplib2.Http()
  response, content = http.request(url+'?'+'currency='+currency, 'GET')
  print content

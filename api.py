import requests, json
import time
import datetime

while True:
   r = requests.get('https://api.hgbrasil.com/finance/quotations?key=127afa60')
   cotacao = json.loads(r.text)

   print('#### cotação ####     ', datetime.datetime.now())
   print('Libra: ',cotacao['results']['currencies']['GBP']['buy'])
   print('Dolar: ',cotacao['results']['currencies']['USD']['buy'])
   print('Euro: ',cotacao['results']['currencies']['EUR']['buy'])
   print('Bitcoin: ',cotacao['results']['currencies']['BTC']['buy'])
   time.sleep(2)
  
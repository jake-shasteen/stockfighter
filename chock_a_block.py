#!/usr/bin/env python
import datetime, os, requests, time

account = raw_input( 'What is your account?' )
venue = raw_input( 'What is the venue?' )
stock = raw_input( 'What is the stock?' )
total = raw_input( 'How much do you want to buy total?' )
price = raw_input( 'What is your maximum buy price?' )

headers = { 'X-Starfighter-Authorization': os.environ.get('STARFIGHTER_API_KEY') }

new_order = 'https://api.stockfighter.io/ob/api/venues/' + venue + '/stocks/' + stock + '/orders'

body = {'account': account, 'venue': venue, 'stock': stock, 'price': price, 'direction': 'buy', 'orderType': 'immediate-or-fill'}
body['qty'] = 100

print 'START'
ts = time.time()
print datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

bought = 0
while bought < total:
  response = requests.post( new_order, data=body, headers=headers )
  bought += response.totalFilled
  print bought
  time.sleep(5)

print 'END'
ts = time.time()
print datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
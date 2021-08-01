import codecs
import json

import requests

# res = requests.get('https://api.coinbase.com/v2/currencies')
# res = requests.get('https://api.coinbase.com/v2/prices/:currency_pair/buy')

is_open = True

while is_open:
    print("Crypto currency")
    print("1 : BTC-BTH")
    print("2 : ETH-BTH")
    print("3 : SLP-BTH")

    choice = input('Please choice currency that u need to look\n If you want to exit enter 0 \n Choice : ')
    res = None

    if choice == '0':
        is_open = False
    elif choice == '1':
        res = requests.get('https://api.coinbase.com/v2/prices/btc-thb/buy')
    elif choice == '2':
        res = requests.get('https://api.coinbase.com/v2/prices/eth-thb/buy')
    elif choice == '3':
        res = requests.get('https://api.coinbase.com/v2/prices/slp-thb/buy')
    else:
        is_open = False

    data = codecs.decode(res._content)
    data = json.loads(data)
    data = data.get('data')
    print('Now 1 of %s have values in %s = %d' % (data.get('base'), data.get('currency'), float(data.get('amount'))))
    print('\n\n\n\n')

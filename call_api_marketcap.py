import json

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = 'https://rest.coinapi.io/v1/assets?filter_asset_id={ETH;SLP;AXS}'
headers = {
    'X-CoinAPI-Key': '11B46C0A-7516-4238-B471-4CBB93C5C744',
    'Accepts': 'application/json',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

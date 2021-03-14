from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class getPrices:
    @staticmethod
    def getPrice(crypto):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': crypto,
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'be18c909-7707-4067-b846-a6dfbb19090e',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            price = data['data']["BTC"]['quote']['USD']['price']
            print(price)
            return price
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

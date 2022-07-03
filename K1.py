import requests

"""
Concepts to rehearse:
    1. python types: classes and dictionaries
    2. IDE with debugging
    3. basic unit tests
    4. basic git and GitHub flow
    5. python virtual environment
"""

class ExchangeRate:
    url = 'http://api.nbp.pl/api/exchangerates/tables/a/?format=json'

    def __init__(self):
        self.table = requests.get(self.url).json()

    def get_currency(self, code: str) -> float:
        currency = 0.0
        for val in self.table:
            for k,v in val.items():
                if k == 'rates':
                    for d in v:
                        if d['code'] == code:
                            currency = d['mid']

        ## BODY TO BE WRITTEN THAT extracts currency from self.table for provided code
        return currency

if __name__ == "__main__":
    exchange = ExchangeRate()
    print(f"1 USD = {exchange.get_currency('USD')} PLN")
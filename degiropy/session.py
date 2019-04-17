import json
import requests
from .config import Config
from .credentials import credentials 
from .cash import Cash
from .portfolio import Portfolio

class Session:
    def __init__(self, sessionid):
        self.sessionid = sessionid
        self.config = self.get_config()
        self.accountid = self.get_account_id()
        self.cash = None

    @staticmethod
    def login():
        data = json.dumps({
            'username': credentials['username'],
            'password': credentials['password']
        })
        response = requests.post(Config.login_url, data)
        result = response.json()
        session_id = result['sessionId']
        return Session(session_id)

    def get_account_id(self):
        response = requests.get(self.config.paUrl + 'client?sessionId=%s' % self.sessionid)
        result = response.json()
        return result['data']['intAccount']

    def get_config(self):
        return Config.from_url(self.sessionid)

    def get_cash(self):
        self.cash = Cash.from_url(self)
        return self.cash

    def get_portfolio(self):
        self.portfolio = Portfolio.from_url(self)
        return self.portfolio

    def get_portfolio_csv(self):
        csv_url = settings.portfolio_csv_url
        accountid = self.accountid
        sessionid = self.sessionid
        request_url = '{}?intAccount={}&sessionId={}&country=NL&lang=nl'.format(csv_url,accountid,sessionid)
        response = requests.get( request_url )
        return Portfolio(response.text,settings.lang)

    def __str__(self):
        s  = "username:  {}\n".format(credentials["username"])
        s += "sessionid: {}\n".format(self.sessionid)
        s += "accountid: {}\n".format(self.accountid)
        return s

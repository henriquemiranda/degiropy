import unittest
from degiropy import Session

class LoginTest(unittest.TestCase):

    def test_login(self):
        #login
        s = Session.login()
        print(s.config)

        #cash
        s.get_cash()
        print(s.cash)
        
        #portfolio
        portfolio = s.get_portfolio()
        print(portfolio)

if __name__ == "__main__":
    unittest.main()

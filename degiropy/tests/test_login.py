import unittest
from degiropy import Session

class LoginTest(unittest.TestCase):

    def test_login(self):
        #login
        s = Session.login()

        s.get_cash()
        print(s.cash)
        
if __name__ == "__main__":
    unittest.main()

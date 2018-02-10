import unittest
from degiropy import Session

class LoginTest(unittest.TestCase):

    def test_login(self):
        #login
        s = Session.login()

if __name__ == "__main__":
    unittest.main()

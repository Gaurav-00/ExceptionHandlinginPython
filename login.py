import unittest
def logincredential(username,password):
    if username=="admin" and password=="12345":
        return True
    else:
        return False

class Logincredential(unittest.TestCase):
    def test_login(self):
        username="admin"
        password="12345"
        result=logincredential(username,password)
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()

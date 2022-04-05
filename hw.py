#to find biggest two number
import unittest

def checkbig(x,y):
    if(x>=y):
        return x
    else:
        return y

class biggest(unittest.TestCase):
    def test_iffirstbigger(self):
        x=20
        y=10
        result=checkbig(x,y)
        self.assertEqual(x,result)
    def test_ifsecondbigger(self):
        x=10
        y=20
        result=checkbig(x,y)
        self.assertEqual(y,result)



if __name__ == "__main__":
        unittest.main()

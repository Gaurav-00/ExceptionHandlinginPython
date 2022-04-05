import Calculate
import unittest
class Calculator(unittest.TestCase):

    def test_add(self):
        x=10
        y=20
        result=Calculate.add(x,y)
        self.assertEqual(result,x+y)

    def test_mul(self):
        x=10
        y=20
        result=Calculate.mul(x,y)
        self.assertEqual(result,x*y)

    def test_sub(self):
        x=20
        y=10
        result=Calculate.sub(x,y)
        self.assertEqual(result,x-y)

    def test_div(self):
        x=20
        y=10
        result=Calculate.div(x,y)
        self.assertEqual(result,x/y)

if __name__=="__main__":
    unittest.main()
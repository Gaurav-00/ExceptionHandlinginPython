import Calculate
import unittest
class Calculator(unittest.TestCase):
    def setUp(self):  #it is use to initialize the values inside a class
        self.x=30
        self.y=24
    def tearDown(self):   #for cleaning value
        self.x=0          #ALWAYS use both setup and teardown
        self.y=0

    def test_add(self):

        result=Calculate.add(self.x,self.y)
        self.assertEqual(result,self.x+self.y)

    def test_mul(self):

        result=Calculate.mul(self.x,self.y)
        self.assertEqual(result,self.x*self.y)         #validate

    def test_sub(self):

        result=Calculate.sub(self.x,self.y)
        self.assertEqual(result,self.x-self.y)

    def test_div(self):

        result=Calculate.div(self.x,self.y)
        self.assertEqual(result,self.x/self.y)

if __name__=="__main__":
    unittest.main()
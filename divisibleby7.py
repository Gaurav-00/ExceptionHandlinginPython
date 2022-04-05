#assertTrue assertFalse  assertalmostequal
import unittest
def volume(x):
    return x**3;
def checkdivision(x):  #number divisible by 7 or not
    if x%7==0:
        return True
    else:
        return False

class checkdivisibleby7(unittest.TestCase):
        def test_case_divisible(self):
            x = 14
            result = checkdivision(x)
            self.assertTrue(result)  # if result is true

        def test_case_divisible(self):
            x = 15
            result = checkdivision(x)
            self.assertFalse(result)  # if result is False
class checkvolume(unittest.TestCase):
    def test_volume(self):
        x=5.5
        result=volume(x)
        self.assertAlmostEqual(result,x**3)
if __name__ == "__main__":
    unittest.main()

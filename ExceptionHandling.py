'''try:
    a=10
    b=0
    c=a/b     #ZeroDivisionError: division by zero  is the error occur in code
    print(c)
except ZeroDivisionError as e:
    print("Exception occur"+str (e))
'''
'''
try:
    age=10
    if age<18:
        raise ValueError("Not eligible to vote")  #to create your own exception use this
    a=10
    b=0
    c=a/b     #ZeroDivisionError: division by zero  is the error occur in code
    print(c)
except ZeroDivisionError as e:
    print("Exception occur"+e)
except :
    print("Program executed Successfully")
else:   #this code executes if no error occur in code in exception handling and it will not work if any exception occur in code
    print("Program execute succesfully"

    #option to create user defined exception
'''
#Automations in python
def add(a,b):
    return a+b

   # (add(2,3))  -::if these line used then it is automation testing

#unittest  By default module in python
import unittest    #to import module
class Myapp(unittest.TestCase):
    #Testcase means maximum form of testing

    def test_case1(self): #this is 1 test case
        a=10
        b=20  #if you do not want to give any instruction to function use pass
        result=add(a,b)
        self.assertEqual(a+b,result)

    def test_case2(self):
        a=12.5
        b=22.5
        result=a+b
        self.assertEqual(a+b,result)

'''finally:         #Below finally code always executes
    print("Harman Ltd.")
    print("Exception Handling done")'''
if __name__=="__main__":
    unittest.main()





'''

    import unittest
def add(x,y):
    return x+y

def check(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
class Myapp1(unittest.TestCase):
    def test_case3(self):
        a=10
        b=22
        c=add(a,b)
        self.assertEqual(a+b,c)
    def test_case4(self):
        a=12.5
        b=13.4
        c=add(a,b)
        self.assertEqual(c,a+b)

class EvenOrAdd(unittest.TestCase):
    def test_case_even_check(self):
        x=10
        result=check(x)

        self.assertEqual("even",result)
    def test_case_odd_check(self):
        x=9
        result=check(x)
        self.assertEqual("odd",result)

if __name__=="__main__":
    unittest.main()

'''

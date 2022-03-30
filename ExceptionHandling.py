'''try:
    a=10
    b=0
    c=a/b     #ZeroDivisionError: division by zero  is the error occur in code
    print(c)
except ZeroDivisionError as e:
    print("Exception occur"+str (e))
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
    print("Program execute succesfully")
finally:         #Below finally code always executes
    print("Harman Ltd.")
    print("Exception Handling done")

    #option to create user defined exception


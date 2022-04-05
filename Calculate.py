def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

if __name__=="__main__":   #this like your main function in c++ where program execution start
    x = int(input("Enter first number-  "))  #to duplicate line move cursor to the end of line and press 'ctrl+d'
    y = int(input("enter 2nd number-  "))
    print(add(x,y))
    print(sub(x,y))
    print(mul(x,y))
    print(div(x,y))

import math

x = int()
y = int()

def Add(a, b):
    global x
    x = a+b
    return

def Sub(a, b):
    global x
    x = a-b
    return

def Multi(a, b):
    global x
    x = a*b
    return

def Divide(a, b):
    global x
    x = a/b
    return

def Power(a, b):
    global x
    x = pow(a, b)
    return

def Square(a):
    global x
    x = math.sqrt(a)
    return

def ClearCalc():
    global x
    global y
    x = None
    y = None
    return

def Calculator():
    global x
    global y

    exit = False
    
    while exit == False:
        if x == None:
            try:
                x = float(input("Enter first number: "))
            except:
                print("User input is not a number")
        
        try:
            y = float(input("Enter second number: "))
        except:
            print("User input is not a number")
        
        calc = input("What do you wanna do with these numbers? [A]dd, [S]ubtract, [M]ultiply, [D]ivide, [P]ower or [Sq]uare: ").upper()
        
        if calc == "A":
            Add(x, y)
        elif calc == "S":
            Sub(x, y)
        elif calc == "M":
            Multi(x, y)
        elif calc == "D":
            Divide(x, y)
        elif calc == "P":
            Power(x, y)
        elif calc == "SQ":
            Square(x)
        else:
            print("User input not recognised")
        
        print(x)
        
        exitClear = input("[E]xit or [C]lear calculator, press [Enter/Return] to continue: ").upper()
        
        if exitClear == 'E':
            exit = True
        elif exitClear == 'C':
            ClearCalc()

Calculator()
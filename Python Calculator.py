import math 
def SquareRoot (x):
   return math.sqrt(x)
  

def lcm(x, y):  
   
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm  

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
     

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.lcm")
print("6.SquareRoot")
print("7.hcf")


while True:
    
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    
    if choice in ('1', '2', '3', '4','5','7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
          print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2)) 

        elif choice == '7':
          print("The H.C.F of", num1,"and", num2,"is", hcf(num1, num2)) 

        
        next_calculation = input("Do you want to do another calculation (yes/no): " )
        if next_calculation == "no":
          break

    elif choice in ('6'):
        num0 = float(input("Enter a number: "))
        
        if choice == '6':
            print("The SquareRoot of ",num0,"is",SquareRoot(num0))

    else:
        print("Invalid Input")

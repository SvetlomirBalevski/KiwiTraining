''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

class Calculator:

    def __init__(self):
        pass

    # This function adds two numbers
    def add(self, x, y):
       return x + y

    # This function subtracts two numbers
    def subtract(self,x, y):
       return x - y

    # This function multiplies two numbers
    def multiply(self, x, y):
       return x * y

    # This function divides two numbers
    def divide(self,x, y):
       return x / y

if __name__ == '__main__':

    def console_input():
       print("Select operation.")
       print("1.Add")
       print("2.Subtract")
       print("3.Multiply")
       print("4.Divide")
       # Take input from the user
       choise = int(input("Enter choice(1/2/3/4):"))
       return choise


    choise = console_input()

    first = int(input("Enter first number: "))

    second =  int(input("Enter second number: "))

    calc = Calculator

    if choise == 1:
       print(first,"+", second, "=", calc.add(calc,first, second))
    elif choise == 2:
       print(first,"-", second, "=", calc.subtract(calc,first, second))
    elif choise == 3:
       print(first,"*", second, "=", calc.multiply(calc,first, second))
    elif choise == 4:
       print(first,"/", second, "=", calc.divide(calc,first, second))
    else:
       print("Invalid choice", choise)


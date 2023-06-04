"""
This Python program is a simple calcultor, which is designed using different concepts of
python programming like infite loop,exceptions,match etc

This program is completely designed for educational purpose...  
"""
def ask_user():# Function to ask the user for the numbers for calculations
    while True:
        try:
            x=int(input("Enter the first number : "))
        except ValueError:
            print("\n...Entered value is not an integer enter only Integers...\n")
        else:
            break
    while True:
        try:
            y=int(input("Enter the second number : "))
        except ValueError:
            print("\n...Entered value is not an integer enter only Integers...\n")
        else:
            break

    return x,y

def display():# Function to display the information
    print("Press 1 to Add two numbers")
    print("Press 2 to Subtract two numbers")
    print("Press 3 to Multiply two numbers")
    print("Press 4 to Divide two numbers")
    print("Press 5 to calculate Modulo")
    print("Press 6 to Exit the calculator")

def calculate():# Function to perform the mathematical operations
    while True:
        try:
            choice=int(input("Enter your Choice : "))
            match choice:
                    case 1:
                        print("Addition of two numbers")
                        a,b=ask_user()
                        add=a+b
                        print(f"The result is {add}")
                    case 2:
                        print("Subtraction of two numbers")
                        a,b=ask_user()
                        subtract=a-b
                        print(f"The result is {subtract}")
                    case 3:
                        print("Multipliaction of two numbers")
                        a,b=ask_user()
                        multiply=a*b
                        print(f"The result is {multiply}")
                    case 4:
                        print("Division of two numbers")
                        a,b=ask_user()
                        division=a/b
                        print(f"The result is {division}")
                    case 5:
                        print("Modulo of two numbers")
                        a,b=ask_user()
                        modulo=a%b
                        print(f"The result is {modulo}")
                    case 6:
                        print("Thank You")
                        break
                    case _:
                        print("Enter valid choice...")
                        display()
        except ValueError:
            print("\n...Your Choice is not valid...\n")
            display()
        except UnboundLocalError:
            print("Invalid Input of numbers")

if __name__=="__main__":
    print("\n...Welcome to calculator...\n")
    display()
    calculate()

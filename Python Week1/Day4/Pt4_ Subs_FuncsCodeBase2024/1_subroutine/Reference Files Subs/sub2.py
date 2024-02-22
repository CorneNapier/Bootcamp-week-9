"To Do: Predict, then Run, and then Investigate"
def addition():
    # name is a global variable 
    # answer, num1 and num2 are local variables 
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")

"Make"
"To Do:Task1: Modify the code above to use either subtraction or multiplication or division and change the subroutine name respectively"
"To Do:Task2: Add comments to the explain your lines of code"
def multiplication():
    # answer, num1 and num2 are local variables 
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    #Multiplies the user inputs for num1 and num2, stores the result in the variable answer
    answer = num1 * num2
    #Using f string, prints the results of the multiplication 
    print(f"The answer to {num1} x {num2} = {answer}")


# prevents the automatic running of the subroutine when it is imported
# in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":
    addition()
    multiplication()
"Further reading on python functions"
# 


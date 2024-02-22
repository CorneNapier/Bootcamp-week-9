"A subroutine(function) may or may not have a return statement"
"A subroutine(function) may or may not have parameters"

# create function use return statement without parameters and arguments
"To Do: Predict, then Run, and then Investigate"
def user():  # define the subroutine/function user
    name = "Emjay"
    return name
    
myUser = user()
def userName():  # define the subroutine userName
    name = input("What is your name? ")
    print(name)
   


# create function use return statement with parameters and arguments
def addition(num1, num2):# defines the addition function
    answer = num1 + num2
    return answer
    
num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))

myAddition = addition(num1, num2)
    

# prevents the automatic running of the subroutine when it is imported
# in to another python file/application

# "If this file is run directly it will automatically call and run the respective subroutines"

if __name__ == "__main__":
    # call/invoke the subroutine
    userName()
    print(f"Method 2\nYour username is {userName}")

    # call/invoke the functioneName
    "Method 1"
    user()
    print(f"Method 2\nThe answer is {myUser}")

    "Method 2"
    # Assigned the function to the variable myAddition
    addition(num1, num2)
    print(f"Method 2\nThe answer is {myAddition}")
    print(f"Your answer to {num1} + {num2} is {myAddition}")






"""
To Do Task 2: Modify the code in subroutine to convert it to a function thats uses parameters and arguments with a return statement
"""
def sub(num1, num2):  # define the subtraction function
    answer = num1 - num2
    return print(f"The answer to {num1} - {num2} is: {answer}")   

num1 = int(input(("Enter your first number: ")))
num2 = int(input(("Enter your second number: ")))

answer = sub(num1, num2)
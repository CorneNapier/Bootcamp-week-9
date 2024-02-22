
"As your programs become larger and more complex, they need to be broken down into smaller, self-contained sections"
"In python function is a type of subroutine, asubroutine is sequence of instructions to perform a specific task with an identifiable name."

"A subroutine(function) definition is used to define the steps within the subroutine(function)"

"A subroutine(function) may or may not have a return statement"

"A subroutine(function) may or may not have parameters"

"def just defines the subroutine(function)"

"A subroutine(function) is not executed unless the subroutine is called."

"A subroutine(function) call tells the program to branch to the function, execute it and come back to the next statement in the main program"

"Custom built function"  '' # A function that you have created yourself and imported into other programs that you have created.

# Syntax
"""
def subroutine/functionName():
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)

#call/invoke the subroutine/function
subroutine/functionName()


"""

"To Do: Predict, then Run, and then Investigate"
# name is a global variable 
name = "Emjay"
print("Your name is: ", name)

name= input(("What is your name? "))
print("Your name is: ", name)


 # def define the subroutine/function user
def user():
    # name is a now a local variable 
     name = input("What is your name?")
     print(f'Welcome {name}, are you enjoying Python so far?')

#executing subroutine user
user()

# def define the subroutine userName
def userName():
    print(f'Welcome {name}')

# print("Welcome")
#userName()

"To Do: Task 1: Call the subroutine inside a print function with or without f-strings and explain your result"

"Modify/Make"
"To Do: Task 2: Modify the subroutine to ask for address and interest"

'Task 2: Investigate  if __name__ == "__main__":'
'Copy and paste the code block above if __name__ == "__main__":  in the browser to investigate it use'
# if __name__ == "__main__":
# Add comment to explain why it can be used in your program in your own words"
#if __name__ == "__main__": block is commonly used to define a block of code that should only execute if the script is being run directly, as opposed to being imported as a module into another script.
"""
__name__ is a special built-in variable in Python. When a Python script is executed, __name__ is set to "__main__" if the script is being run directly.
When the script is imported as a module into another script, __name__ is set to the name of the module (i.e., the name of the script file).
Therefore, if __name__ == "__main__": checks if the script is being run directly by the Python interpreter.
"""

# call/invoke the subroutine
# call/invoke the subroutine
  
"Knowledge Check"
"Task 4: Linking existing knowledge with new knowledge"
# What do you think is the equivalent of the python 'def' keyword in JavaScript
#function key word

"Further reading on python functions"
# 

def age():
    print(3)

def address():
    print("London")

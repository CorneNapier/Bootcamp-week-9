# Selection is use to control the flow of the program
"""if condition is met:
    code block"""
score = 25
userNum = int(input("Enter a user number:"))
 
if score < userNum:  # check the condition that score(25) is less than userNum(?)
    # do something/execute the code block
    print(f"Good score {userNum}") # f-string

# Selection is used to control the flow of the program

"Predict, then Run, and then Investigate"
# check the condition that pStudy value is same as the value held in curProgram
# do something/execute the line of code if the condition is checked above true/met - welcome
# The block(else) of code will be executed if the condition in the if block is not true/not met

pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"

if pStudy == curProgram:
    print(f'Well done, you are right! Answer: {pStudy}')
else:
    print(f'Try again! Answer: {pStudy}')

"To Do: Q&A"
#!What differs from writing if statement in JS and python ?
#JS uses () for condition and {} for code statement whereas in python condition is written without () and code statment follows : using indentation

score = 26
userNum = int(input("Enter a number: "))


if score == userNum:
    print(f'Hit the nail on the head, score {userNum}')
#JS else if statement syntax differ from python, in JS its: else if (condition){code statement}, in python its: elif condition: indentation then code statement
elif score < userNum:
    print(f'Great score, score {userNum}')
else:
    print('Try again')

#ToDo: Task 1:
"Modify the code above to use any one of the comparison operators below"

# Comparison operator compare values
# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to
# >= 	greater than or equal to
# !=    Not equal to
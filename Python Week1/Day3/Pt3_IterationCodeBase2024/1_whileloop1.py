"""
Use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program

You will need a while statement:
When your program needs to repeat actions, while a condition is satisfied
"""

"To Do: Predict, then Run, and then Investigate"
#sets number variable to the number 4
number = 4
#prints instruction
print("Guess a number between 1 and 10")
#asks for user input
numGuess = int(input("Guess a number between 1 and 10: "))
#the while loop will keep looping until 4 is inputted, once 4 is the answer the loop will exit
while numGuess != number:
   numGuess = int(input("Incorrect\nGuess a number between 1 and 10:"))
print(f"You guessed {numGuess} is correct")




"To Do: Task1: Add comments to the code to explain what the while loop is doing"
"Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp
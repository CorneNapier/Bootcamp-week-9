# for variableName in rangeObject(numberOfIteration)
# for loops that use the range() function
# range() is the sequence that you are going to iterate through
# range() is a built-in function just like input(). 


# range(stop) -> range object range(start, stop[, step]) -> range object
# When you call the range function, you can pass it up to three values: 
# The start number
# The end number
# The step 

"To Do: Predict, then Run, and then Investigate"

"start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3"
for findNum in range(10):
    print(findNum)
#this for loop will start at 0 and iterate through numbers stopping/inlcuding 9.


"Modify/Make"
"Task 2: Create a program that uses a for loop to start count from 1 to and ends at 20 "
for number in range(1,21):
    print(number)
"Task 3: Create a program that uses a for loop to start count  from 1, and increment(step) of 5 a and ends/stop at 30"
for number in range(0,30,5):
    print(number)
"Task 4:  Modify the code you produced in task 3 to count down in steps of 5 (from a high number(30) to a low number greater or equal to 1)"
for number in range(30,-5,-5):
    print(number)

"Further reading on python for statements"
# https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements


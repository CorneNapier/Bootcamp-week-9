"Objectives"
# Use for loops with string operations
# Using a for loop to iterate over a string


searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")

"To Do: Predict, then Run, and then Investigate"
"iterate over a string to find an count a character"
#define subroutine(function) using two parameters
def count_character(searchStr, findChar):
    # we set count to the value of zero
    counter = 0
    # loop through the entire string to search for the character entered
    for aChar in searchStr:
         # check if the character entered is a match with any character in the string
        if aChar == findChar:
             # increase the count by 1 every time you find the same character
            counter += 1
    return counter

result = count_character(searchStr, findChar) #store the results of the subroutine(function) in result
print(f"Found the character : {findChar}, {result} times") # display the result

"To Do: Task 7: Refactor the code above by putting it into a subroutine and call/invoke it."
#Note: if you encounter any errors, copy and paste it in google then apply the solution.

if __name__ == "__main__":
     count_character()

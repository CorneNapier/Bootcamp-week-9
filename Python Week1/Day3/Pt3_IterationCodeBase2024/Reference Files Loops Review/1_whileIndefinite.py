"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""



# import the datetime library/class/module
import datetime


"To Do: Predict, then Run, and then Investigate"



print("None while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))


"To Do: Task 1" 
" study the output of the code above and the output in in the while loop below, and use the links provide to answer"

" What is the while loop doing?"
#The while loop is updating the current time

" add comment to explain what you understand the 'datetime.datetime.now().strftime('%H:%M:%S')'"
# Sets the format of the current time found using datetime.datetime.now() to hrs:mins:Secs

" add comment to explain what you understand the 'end='"
# end=' ' parameter is used with the print() function to specify what should be printed at the end of the output
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

" add comment to explain what you understand the '\r' "
#each update of the loop is printed on the same line
# https://www.w3schools.com/python/gloss_python_escape_characters.asp

" What will output if you remove  , end='\r'  from the while loop"
#it will print the updated current time on a new line

print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")

    # time.sleep(1)

"Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp
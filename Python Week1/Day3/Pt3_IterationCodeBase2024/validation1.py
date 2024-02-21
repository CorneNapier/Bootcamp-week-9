"Task 1: In the terminal Enter numeric values for the first and second number to perform addition and take note of the output "
"Task 2: In the terminal Enter a numeric value  for the first number and string value(ten/one/two) for the second number to perform addition and take note of the output"


try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")
#can use Exception to cover an error that is unknown to you
#can use a tuple to catch more potential errors
except (ValueError, IndexError, IndentationError, Exception) as e:
    if ValueError:
        print(f"{e}: Please Enter Numeric Values")
    elif IndexError:
        print("Please Enter Numeric Values")
    elif IndentationError:
        print("Please Enter Numeric Values")
    else:
        print(e)


print("Executing...some code and processes")


"Task 3: Explain why did the program break, when you followed the instructions in task 2 but not in task 1"
#In this example, if the user enters a value that cannot be converted to an integer (such as a string or a float number), the int() function will raise a ValueError. The except ValueError: block catches this exception, and the code within that block is executed, printing a message indicating that the user should enter a valid integer.


# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception



#name = input("What is your name? ") 

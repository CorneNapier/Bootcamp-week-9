"To Do: Predict, then Run, and then Investigate"



"Modify"
"To Do: Task3: Modify the code below to use a parameter"

name = input("Please Enter Your Name: ")
lname = input("Please enter your last name: ")

def user(name, lname):
    print(f"Your full name is: {name} {lname}")



def userName():  # define the subroutine userName
    # function body(code to execute when the subroutine/function is called)
    name = input("What is your user name? ")
    print(f'Username: {name}, has been found')




# prevents the automatic running of the subroutine when it is imported
# in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
"To Do: Task4: Modify the code below to use an argument when you call/invoke it"
if __name__ == "__main__":
    user(name, lname)
    userName()
    name = input("Please Enter Your Name: ")
    lname = input("Please enter your last name: ")
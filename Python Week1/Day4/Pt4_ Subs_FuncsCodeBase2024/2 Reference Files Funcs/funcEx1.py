"To Do: Task1: Modify the code in userName function below to use parameter and arguments"

def userName(fullName, address, interest):  # define a subrouitine called userName
    print(f"My name is {fullName}, my address is {address} and my interest is {interest}")
    
fullName = input("Enter your name: ")
address = input("Enter your address: ")
interest = input("Any interest? ")

userName(fullName, address, interest)


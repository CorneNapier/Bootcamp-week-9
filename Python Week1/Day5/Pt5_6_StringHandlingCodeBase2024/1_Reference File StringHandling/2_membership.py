"The for loop can be used to iterate through a string and any sequence of elements(eg numbers etc)"

"Objective"
# Using a for loop to iterate over a string
"To Do: Predict, then Run, and then Investigate"
name = "Abdul is Software Technical Trainer"
for letter in name:
    print(letter)

"Objectives"
 # Use a substring in a program
mainString = "Hello mate!"
substring = 'mate!'
 # Use the in operator to check for a substring
if substring in mainString:
    print("The substring '{}' exists in the main string.".format(substring))
else:
    print("The substring '{}' does not exist in the main string.".format(substring))

searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")
# print(searchStr[3])
"""The membership operator can be used to check if a value/substring is present
or not in object and returns true if it does"""
if findChar in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Found {findChar}")
else:
    print(f"Not Found {findChar}")

"Task 5: Replace the in operator above with the 'not in' operator, run the code then explore the output in the terminal "


# Further reading on operators not covered in the bootcamp see links below
"https://www.w3schools.com/python/gloss_python_identity_operators.asp"
"https://www.w3schools.com/python/gloss_python_bitwise_operators.asp"


"To Do: Task 6: use if and 'in' operator to find a character in your name"

name = "Corne Napier"  # Add your name in between the speech marks 
findChar2 = input("Enter character to search for: ")
if findChar2 in name:
    print(f"Found {findChar2}")
else:
    print(f"Not Found {findChar2}")

"Extension and research of using for loop and if statement "

# You have been provided with the vowels in a list data structure and a variable
# name that is assigned with an empty string.


"Your task is to assign your name to the variable called name and use a for loop and if statement to:"
"Iterate through the list of vowels to find the vowels in your name"
"          0,   1  , 2,  3,  4"
vowels = ["a", "e", "i", "o", "u", "j"]  # vowels
name = "Corne Napier"  # Add your name in between the speech marks 
# Iterate through the characters of the name
for char in name:
    # Check if the character is a vowel
    if char.lower() in vowels:
        print(f"{char} is a vowel in your name.")

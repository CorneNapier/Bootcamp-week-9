
"Objective"
"" '' # Describe the function of string operations
"""You can perform operations with string in a similar way to the operations 
that you can perform with numbers. """

"To Do: Predict, then Run, and then Investigate"

"Objective"
"" '' # String handling techniques
stringVal1 = "a" > "b" # check if the letter a is greater than b
print(stringVal1)


stringVal2 = "b" > "a"  # check if the letter b is greater than a
print(stringVal2)

"Task 1 Working with comparison operators" # != , == , <= , >=, <,>
#  use any comparison operator to compare the letter "a" and "A"
stringVal3 = 'a' == 'A'
print(stringVal3)
#  use any comparison operator to compare the letters "ax" and "ZZ"
stringVal4 = 'ax' > 'ZZ'
print(stringVal4)
#  use any comparison operator to compare your firstname with any another first name
stringVal5 = 'Corne' < 'John'
print(stringVal5)

"You can multiply a string, it will concatenate the same value for the number of times stated."
mutiplyWord = "Python\n" * 5  # mulitply the word n times
print(mutiplyWord)

"""The + sign concatenates (joins) the two string together.
There is no space because it hasn't been given that instruction"""
joinWords = "Python" + "Java"  # join the two words
print(joinWords)

"Task 2"
# Create two variables fName and lName and join and print them using a variable called fullName
fname = 'Peter'
lname = 'Parker'
fullName = fname + ' ' + lname
print(fullName)

"Objective"
"" '' # Finding the length of a string len()

"Knowledge Check: What is the len() used for in a string?"
#The amount of characters used in a string, including spaces and punctuation

course = "Python"
wordLength = len(course)
print(wordLength)

"Objective"
"" '' # Finding a character using indexing e.g. course[0]

"Task 3: How can we print a specific character using the index value or position in a string or list?"
findChar = course[3]
print(findChar)

"Objective"
# Make/modify a program that uses string-handling techniques
def count_vowels_consonants(text):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count

def main():
    text = input("Enter a text: ")
    vowel_count, consonant_count = count_vowels_consonants(text)
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)



"Task 4: Write the code to print the letter  h"
"Hints"
course = "Python Programming"
wordLength = len(course)
print(f"The length of the string {course} is {wordLength}")
print(course[3])

"Objective"

"" '' #Extension activity: Research and independent learning activity
"Task 1: Return all the characters from the string held in the course variable using negative values"
courseCharReversed = course[::-1]
print(courseCharReversed)
"Task 2: Research and independent learning activity"
# Open the Python documentation using the provided link to discover uses of :
# str.capitalize()
# str.title()
# str.swapcase()
# https://docs.python.org/3.3/library/stdtypes.html?highlight=substring#string-methods

if __name__ == "__main__":
    main()
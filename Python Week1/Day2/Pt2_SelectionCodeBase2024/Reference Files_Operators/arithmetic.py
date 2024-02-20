"Arithmetic expression evaluates to a number"

num1 = 10  # static object/value
num2 = 5  # static object/value
num3 = 11  # static object/value
num4 = 2  # static object/value

# + operator is use for adddition and also concatenation(join things)

print("Addition: " + str(num1) + " + " + str(num2) + "=", num1 + num2)

# Using f-strings to format print statement (f followed by quotes)
# strings cater for all data types

# plus operator +
print(f"Using f-strings\nAddition: {num1} + {num2} = { num1 + num2} ")

"To Do: Task 1: What is the equivalent of f-strings in JavaScript?"
#template literals = `Example of f string in ${js}`. Allows you to use variables in a string

"Review the code below to answer the following questions"
"Task 1: Explain in your own words the operators listed below "
# Division (/)
#divides a number by another number. When you divide one number (the dividend) by another (the divisor), you're essentially finding out how many times the divisor can be subtracted from the dividend without resulting in a negative number.

# Floor Division (//)
#rounds the result down to the nearest whole number using division

# Modulus (%)
#is used to find the remainder of the division of two numbers. 

"To Do: Explain in your own words when you would use the oprators listed above"
#division = used where you need to accurately represent fractional parts of the result.
#floor division = Distributing items equally among a certain number of people
#modulus = checking if a number is even or odd

# division /
print(f"Division (/): {num3} / {num4}  = {num3 / num4}")

# Floor division
print(f"Floor division (//): {num3} / {num4}  = {num3 // num4}")

# Modulus %
print(f"Modulus (%): {num3} / {num4}  = {num3 % num4}")


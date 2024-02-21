"To Do: Predict, then Run, and then Investigate "

countries = ["Scotland", "Spain", "England", "Wales", "Brazil", "Argentina", "Italy","France"]


print("Printed all countries in the terminal")
for country in range(len(countries)):
     print(f"{countries[country]}")


print("\nNot all countries are printed in terminal")
for country in range(2):
    print(f"{countries[country]}")

"To Do: Task 1: Explain why the first loop printed all the countries and the second for loop did not"
#The first loop uses the entire length of the list using range(len()), where as the second loop uses a range() stopping at 5.

"Modify"
"To Do: Task 2: Modify the number in the second for loop range function from '5' to any other number and explain the output"
# Changed the range() in the second loop to stop at 2, meaning it will only show the first two countries in the countries list then stop the loop.

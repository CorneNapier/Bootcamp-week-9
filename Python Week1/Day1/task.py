"Dictionaries"
#It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

#example of a dictionary being created
members = {'John': 4305, 'Chris': 6789}

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:

#Looping through a dictionary
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)
    
#     "results of this loop would be:"
#     #gallahad the pure
#     #robin the brave
    
employees = {
        1001: "John Smith",
        1002: "Alice Johnson",
        1003: "Bob Brown"
    }
    
    #Accessing values
print("Employee with ID 1002", employees[1002])
    
    #adding new employee
employees[1004] = "Emily Davis"
print("Employee with ID 1004", employees[1004])
    
    #iterating over dictionary
for emp_id, emp_name in employees.items():
        print(f"Employee ID: {emp_id}, Employee Name: {emp_name}")
    
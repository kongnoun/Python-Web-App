# Creating a dictionary
empty_dict = {}
person = {
    "name": "John",
    "age": 30,"city": 
    "New York"
    }

dict_constructor = dict(name="John", age=30, city="New York")
from_tuples = dict([("name", "John"), ("age", 30), ("city", "New York")])

print(dict_constructor)
print(from_tuples)

squares = {x: x**2 for x in range(5)}

print(squares)
print(squares[2])

# Print(person[0]) dictionary cannot be accessing using index, it should be accessed using key

print(person["name"]) # This will print "John"

print(person["age"]) # This will print 30

print(person["city"]) # This will print "New York"

# The error in the previous line was due to incorrect syntax. The correct syntax is to use the key name in square brackets, not a colon-separated key-value pair.

print(person.get("name")) # This will also print "John"
print(person.get("age")) # This will also print 30
print(person.get("city")) # This will also print "New York"
print(person("country", "USA")) # This will print "USA" because the key "country" does not exist in the dictionary, so it returns the default value provided.

#=====================================================
# Accessing into dictionar
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "university": "XYZ University"
    }
}
print(person.get("age")) # This will print 30
print(person.get("country", "USA")) # This will print "USA" because the key "country" does not exist in the dictionary, so it returns the default value provided.
country = person.get("country")
if country == None:
    country = "Empty Inside IF"
print(country) # This will print "Empty Inside IF" because the key "country" does not exist in the dictionary, so it returns None, and the if condition is satisfied, assigning "Empty Inside IF" to the variable country.

#=======================================================
# How to add & update dictionary
user = {}

user["username"] = "john_doe"
user.update({"password": 123456, "username": "john_doe_updated", "capcha": "abc123"})
user.setdefault("usernam", "john_doe") # This will set the key "usernam" to "john_doe" if it does not already exist in the dictionary. Since "usernam" does not exist, it will be added to the dictionary with the value "john_doe".
user.setdefault("age", 30) # This will set the key "age" to 30 if it does not already exist in the dictionary. Since "age" does not exist, it will be added to the dictionary with the value 30.
print(user) # This will print {'username': 'john_doe_updated', 'password': 123456, 'capcha': 'abc123', 'age': 30}

# How to remove items from dictionary
user.pop("password") # This will remove the key "password" and its associated value from the dictionary. If the key does not exist, it will raise a KeyError.
user.popitem() # This will remove and return the last key-value pair added to the dictionary.
print(user) # This will print {'username': 'john_doe_updated', 'age': 30}

removed_value = user.pop("username")
print(removed_value)
print(user) # This will print {'age': 30}

removed_value = user.pop("age")
print(removed_value)
update_value = user.update({"username": "john_doe_readded"}) # This will add the key "username" with the value "john_doe_readded" back to the dictionary. If the key already exists, it will update its value.
print(user) # This will print {'username': 'john_doe_readded'} 


#=======================================================
# Looping through key 
for key in user:
    print(f"Key: {key}, Value: {user[key]}") # This will print the key and its associated value for each key in the dictionary.

#------------------------------------------------------
    
# Looping through items can get both key, value from item insdie dictionary
for key, val, in user.items():
    print(f"Key: {key}, Value: {val}") # This will print the key and its associated value for each key-value pair in the dictionary.
    
#-------------------------------------------------------

# Looping through values can get only value from item insdie dictionary
for val in user.values():
    print(f"Value: {val}") # This will print the value for each key in the dictionary.

#-------------------------------------------------------

# Iterating Over Dictionaries
# Iterate over keys
for key in person:
    print(f"{key}: {person[key]}")
# Iterate over key-value pairs (preferred)
for key, value in person.items():
    print(f"{key}: {value}")
# Iterate over values only
for value in person.values():
    print(value)   
    
# Practical Examples    
# 1. Counting occurrences: Use dictionaries to count frequency of items
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

clean_text = text.replace(" ", "")
print(clean_text)

before_join = text.split(" ")
print(before_join)
clean_text = "".join(text.split(" "))
print(clean_text)


# 2. Grouping data: Organize related items together.
students = [
{"name": "Alice", "grade": "A"},
{"name": "Bob", "grade": "B"},
{"name": "Charlie", "grade": "A"},
]
by_grade = {}
for student in students:
    grade = student["grade"]
if grade not in by_grade:
    by_grade[grade] = []
by_grade[grade].append(student["name"])












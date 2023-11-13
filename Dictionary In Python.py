"""
                                        DICTIONARY
A dictionary is a mutable and unordered collection of key-value pairs. Each key in a dictionary
must be unique, and it is associated with a corresponding value. Dictionaries are often used for
efficient data retrieval and storage, as you can quickly access values using their associated
keys.
"""
# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Accessing values using keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Modifying values
my_dict['age'] = 26

# Adding a new key-value pair
my_dict['gender'] = 'Male'

# Iterating over keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
if 'city' in my_dict:
    print("City exists:", my_dict['city'])

#Dictionary Example
dic = {
    1 : "Zaid",
    2 : "Bakar",
    3 : "Uzyr",
    4 : "Zuhair"
}
# print(dic[1])
# print(dic)

#Methods in Dictionary

dic2 = {
    5 : "Sj",
    6 : "Faizan",
    7 : "Abdul Rehman",
    8 : "Abdul Mateen"
}
dic.update(dic2)
print(dic)
dic2.clear()
print(dic2)
dic.popitem(5)
print(dic)
print(dic2)



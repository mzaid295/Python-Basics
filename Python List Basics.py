"""
A Python list is a built-in data structure that represents an ordered collection of elements.
Lists are versatile and can store items of various data types, such as numbers, strings, and even other lists.
Lists are enclosed in square brackets [ ] and are separated by commas. They allow for indexing, slicing, appending,
and modifying elements, making them a fundamental and widely used data structure in Python. Lists are mutable,
meaning you can change their content after creation, and they are commonly used for tasks like storing
and managing data in a flexible and dynamic manner.
"""
list = [2,13,14,8,16,17,"Cash"]
print(list)

#Indexing of list
print(list[0:5])

#Appending a value in list
list.append(9)
print(list)

#List Sorting
list2= [10,9,8,7,6,5,4,3,2,1]
list2.sort()
print(list2)

#Adding value in a list with the index number
list2.insert(1,69)
list2.count()

#append the value at the end of the list
list3= [10,9,8,7,6,5,4,3,2,1,10,11]
list3.append(78)
print(list3.count(78))

#Extending the list
list2.extend(list3)
print(list2)
list2.sort()
print(list2)
print(list2.count(2))

#Concetinate the list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2

print(concatenated_list)

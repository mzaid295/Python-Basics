"""
                                      TUPLES IN PYTHON
A tuple is a collection data type that is similar to a list in many ways, but with one key difference:
tuples are immutable. This means that once you create a tuple, you cannot change its contents (add, remove,
or modify elements). Tuples are defined by enclosing a sequence of elements in parentheses (), separated by commas..
"""
#Tuple and its Functions with indexing
tup = (1,2,3,7,4,5,6,8,9)
print(type(tup), tup)
print(tup[-1])
print(tup[0])
print(tup[2])

j = int(input("Enter the value: "))
if j in tup:
    print("Yes, its available in tupple")
else:
    print("Please Enter Value In String")

#Creating second tupple
tup2 = tup[1:4]
print(tup2)

#operations on tupple
tup = ("Pakistan","Germany","France")
print(type(tup)) #Type of tupple
ttl = list(tup) #Converting tupple to list, to do some changes.
print(type(ttl))
ttl.append("Lahore") #Adding the values to list
print(ttl)
ttl.insert(0,"UAE") #Inserting the value according to index number
print(ttl)

"""
MUHAMMAD ZAID
"""
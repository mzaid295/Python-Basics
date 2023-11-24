"""
 Encapsulation is one of the fundamental principles of object-oriented programming (OOP).
 It refers to the concept of bundling the data (attributes) and the methods (functions) that operate on the
 data into a single unit called a class. Encapsulation helps in organizing the code in a way that hides the
 internal implementation details of an object from the outside world and restricts direct access to some of
 its components.

There are three main levels of access control in Python:

Public: Members (attributes and methods) declared public are accessible from outside the class. In Python,
by convention, all members are public unless they are marked as private or protected.

Protected: Members declared protected are accessible within the class and its subclasses. In Python, this
is achieved by prefixing the name of the member with a single underscore _.

Private: Members declared private are not accessible from outside the class. In Python, this is achieved by
prefixing the name of the member with two underscores __.
"""


class MyClass:
    def __init__(self):
        # Public attribute
        self.public_var = 10

        # Protected attribute
        self._protected_var = 20

        # Private attribute
        self.__private_var = 30

    def public_method(self):
        print("Public method called")

    def _protected_method(self):
        print("Protected method called")

    def __private_method(self):
        print("Private method called")


# Creating an instance of MyClass
obj = MyClass()

# Accessing public members
print(obj.public_var)
obj.public_method()

# Accessing protected members
print(obj._protected_var)
obj._protected_method()

    # Creating an instance of MyClass
    obj = MyClass()

    # Accessing public members
    print(obj.public_var)
    obj.public_method()

    # Accessing protected members
    print(obj._protected_var)
    obj._protected_method()

# Accessing private members (Note: This will raise an AttributeError)
# print(obj.__private_var)
# obj.__private_method()

#2nd Example
    def __display(self):   # Private method
        print(f"Name: {self.__name}, Age: {self.__age}")


    def get_details(self):
        self.__display()    # Accessing the private method within the class


# Creating an instance of the class
person = Person("ZAID", 30)


# Accessing private attributes directly will raise an error:
# print(person.__name)  # This will result in an AttributeError


# Accessing private method via a public method
person.get_details()  # This prints "Name: Faizan, Age: 30"




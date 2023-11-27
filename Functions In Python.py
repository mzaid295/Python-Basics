"""
----------------------------------------- F U N C T I O N - IN - P Y T H O N -----------------------------------------
Function is a block of reusable code that performs a specific task. Functions provide modularity and help in
organizing code by breaking it into smaller, manageable pieces. Here's a basic syntax for defining a function in
Python:
"""

def gmean(a = 0,b = 0):
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    x = (a + b)
    print(x)


def spellcount (a=0):
    name2 = str(input("Enter the value of A: "))
    print(name2,"have", len(name2), "characters")

def license (a=0):
    age = int(input("Please Enter Your Age: "))
    print("Your age is:", age)
    if (age > 18):
        print("Congratulations!! You are eligible for driving license")
    # if (age == 18):
    #     print("Congratulations!! You are eligible for driving license")

    elif (age < 18):
        print("Oops!! You are not eligible for driving license")

    else:
        print("Please write in numbers only")

gmean()
slice()
license()
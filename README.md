# QUESTION: In a company, one of these values have to be associated with the employee of the company as
# their designation. You have to provide the self explanatory python example code as answer that
# how can we use them.
# CEO, Director, Manager, Clerk, Salesman, Receptionist, Driver, Peon
# ANSWER:
user = int(input("Enterthe values: "))
dict = {"CEO": 1,
        "DIRECTOR": 2,
        "MANAGER" : 3,
        "CLERK" : 4,
        "SALESMAN" : 5,
        "Receptionist": 6,
        "DRIVER": 7,
        "PEON":8}
s = list(dict)
# print(dict)
if user == 1:
    print(s[0])
# ------------------
if user == 2:
    print(s[1])
# ------------------
if user == 3:
    print(s[2])
# ------------------
if user == 4:
    print(s[3])
# ------------------
if user == 5:
    print(s[4])
# ------------------
if user == 6:
    print(s[5])
# ------------------
if user == 7:
    print(s[6])

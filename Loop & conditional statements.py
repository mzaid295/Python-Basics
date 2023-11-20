#Python Conditional Statements\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////////////
age = int(input("Please Enter Your Age: "))
print("Your age is:",age)
if (age>18):
    print("Congratulations!! You are eligible for driving license")
# if (age == 18):
#     print("Congratulations!! You are eligible for driving license")

elif(age<18):
    print("Oops!! You are not eligible for driving license")

else:
    print("Please write in numbers only")
#------------------------------------------------------------------------------
#Checking the value negative, postive and zero
value = int(input("Enter the value to check negative, postive and zero: "))
if (value > 0):
    print("The value is positive")
elif (value < 0):
    print("The value is Nagative")
elif (value == 0):
    print("The value is zero")

# String and numbers (Strings are immutable we cannot edit this)
w = "string"
print("The data type of W is:",type(w))
print("I am converting the text in Upeercase:",w.upper())
print("I am converting the text in Lowercase:",w.lower())
print(w.replace("string","InvoZone"))

e = 5
print("The data type of W is:",type(e))
#strings in python
print('''Hello InvoZone, I am Muhammad Zaid 5
"This is written by Zaid"''')

for chracter in w:
    print(chracter)

#FOR LOOP\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////
colors = ['Red','Blue','Green','White']
for color in colors:
    print(color)
for colors in range(3):
    print(color + 1)

#While LOOP\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////////////////
num = int(input("Enter the number: "))
while (num + 1):
    print(num, "Even number")
else:
    print("odd number")
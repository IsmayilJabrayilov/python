#Write a Python program that asks the user to enter a number and prints whether it is positive, negative, or zero.


num = int(input("Enter number:"))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is 0" )
else:
    print("Wrong input")
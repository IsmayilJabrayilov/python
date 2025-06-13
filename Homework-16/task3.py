#Write a Python program that takes a user's name as input and prints a greeting message. 
#If the name is "Alice" or "Bob", the program should print "Hello, Alice/Bob!" Otherwise, it should print "Hello, guest!".

name = str(input("Please input your name: "))

if (name == 'Alice' or name == 'Bob'):

    print("Hello", name)
else:
    print("Hello Guest")
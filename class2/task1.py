age=int(input("Input your age: "))

if (age>0 and age<13):
    print("child")
elif (age>=13 and age<18):
    print("Teenager")
elif (age>=18 and age<65):
    print("adult")
elif (age>=65):
    print("elder")
else:
    print("wrong age")
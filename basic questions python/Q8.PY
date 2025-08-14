"""to check a number is positive negative or zero"""

num=int(input("enter a number : \t"))

if num>0:
    print("positive")
elif num==0:
    print("zero")
elif num<0:
    print("negative")
else:
    print("invalid input")
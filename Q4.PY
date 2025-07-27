"""SWAPPING OF TWO NUMBERS"""

a=int(input("enter number a"))
b=int(input("enter number b"))

a,b=b,a    #method 1

print(a,b)

temp=a
a=b
b=temp

print(a,b)
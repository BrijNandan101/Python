"""FIND THE LARGEST AMONG THREE NUMBERS"""

a=int(input("a"))
b=int(input("b"))
c=int(input("c"))


print(max(a,b,c))  #method 1

maxvalue= a if (a>b and a>c) else (b if b>a and b>c else c)   #method 2

print(f"max number is {maxvalue}")
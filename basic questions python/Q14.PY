
"""print factorial of a number"""

num=int(input("enter number \t"))

if num<=0 and num==1:
    print("1")
fact=1
for i in range(1,num+1):
    fact=fact*i

print (f"The factorial is {fact}")
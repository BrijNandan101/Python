"""CHECK FOR PRIME"""

num=int(input("enter a num \t"))

if num==1:
    print("not prime")
if num>0:
    for i in range(2,num):
        if num%i==0:
            print("not a prime")
            break
    else:
        print("prime")
"""PRINT ALL PRINT IN RNAGE"""
list=[]

LowRANGE=int(input("ENTER LOWER RANGE\t"))

upperRANGE=int(input("ENTER UPPER RANGE\t"))

if LowRANGE<2:
    print("lowrange invalid")

for i in range(LowRANGE,upperRANGE+1):
    isPrime=True
    for j in range(2,int(i**0.5)+1):

        if i%j==0:
            isPrime=False
            break
    if isPrime:
        list.append(i)        

print(list)
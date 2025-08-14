"""FIND THE SQUARE ROOT OF GIVEN NUMBER"""
import math

num=int(input("Enter the number\t"))

sr1=num**0.5    #method 1 of doing it

sr2=math.sqrt(num)  #method 2 


print (f"by method1 { sr1}")
print(f"by method2 {sr2}")
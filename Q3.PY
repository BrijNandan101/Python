"""SOLVE A QUADRATIC EQUATION"""
#a,b,c should be real numbers
#a is not equal to 0

import cmath

a=int(input(("enter a: \t")))
b=int(input("enter b : \t"))
c=int(input("enter x : \t"))

determinant= b**2-(4*a*c)

root1= (-b - cmath.sqrt(determinant))/(2*a)
root2= (-b + cmath.sqrt(determinant))/(2*a)

print(f"determinant is : {determinant}")
print(f"1st root is : {root1}")
print(f"2nd root is : {root2}")
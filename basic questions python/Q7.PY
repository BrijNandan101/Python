"""TEMPERATURE CONVERSION"""

# 0 CELSIUS= 32 FARANHEIT

# (c*9/5)+32 =Farenheit

temp=float(input("Enter temperature in celsius \t"))

convert=(temp*9/5)+32

print(f"Temperature in Farenheit is : {convert:.2f}degree")
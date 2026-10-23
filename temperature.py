unit=input("is temperature in celsius or fahrenheit?(C or F): ")
temp=float(input("enter the temperature:"))
if unit=="C":
    temp=(temp*9/5)+32
    print(f"temperature in fahrenheit is {temp} F")
elif unit=="F":
    temp=(temp-32)*5/9
    print(f"temperature in celsius is {temp} C")
else:
    print(f"{unit} is an invalid unit")
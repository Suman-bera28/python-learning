# python weight converter

weight=float(input("enter your weight: "))
unit=input("kilogram or pounds?(K or L): ")
if unit =="k":
    weight=weight*2.205
    unit="Lbs."
elif unit=="L":
    weight=weight/2.205
    unit="Kgs."
     
else:
    print(f"{unit} was not valid")
    

print(f"your weight is {weight} {unit}")
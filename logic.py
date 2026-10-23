
#or operator
# temp=input("enter temperature:")
# is_raining=False
# temp=(int(temp))
# if temp > 35 or temp<0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

#and operator
temp=int(input("enter temperature:"))
is_sunny=True

if temp>=28 and is_sunny:
    print("it's hot outside")
    print("it's sunny")
elif temp<=0 and is_sunny:
    print("it's cold outside")
    print("it's sunny")
        
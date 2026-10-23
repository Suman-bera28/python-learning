name=input("entr yr name: ")
while name=="":
    name=input("entr yr name: ")
age=int(input("enter your age: "))

while age=="":
    age=int(input("enter your age: "))

while age<0:
    print("age can't be less than 0")
    age=int(input("enter your age: "))

print(f"hello {name}")
print(f"you are {age} years old")
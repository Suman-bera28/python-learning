age=int(input("entr yr age: "))
has_ticket=True
price=10.00


if age>=65:
    print("you are going to retire")
    print(f"the ticket price for a retire person is ${price*0.25}")

elif age>=18:
    print("you are an adult")
    print(f"the ticket price for a adult  is ${price}")
    


else:
    print("you are a child")
    print(f"the ticket price for a child is ${price*0.75}")


if has_ticket:
    print("you may enter,you have a ticket")
else:
    print("you need to buy a ticket")

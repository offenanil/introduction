print("===========COMPUTER BAZAR=============")
a = input("enter the options for computers")
a = int(a)
if a == 1:
    print(" 1. dell(20000)")
    cost1 = int(20000)
elif a == 2:
    print("2.mac(50000)")
    cost1 = int(50000)
elif a == 3:
    print("3.Toshiva(3000)")
    cost1 = int(30000)
else:
    print("enter options between 1 to 3")
delivery_quantity = input("enter the amount of quantity you want")
delivery_quantity = int(delivery_quantity)
print(delivery_quantity)
delivery_type = input("enter 1 for home delivery and 2 for pick up")
delivery_type = int(delivery_type)
if delivery_type == 1:
    print("delivery charge is 1000")
    cost2 = int(cost1 + 1000)
elif delivery_type == 2:
    print("free")
    cost2 = int(cost1 + 0)
else:
    print("enter valid number")
packaging = input("enter the packaging options")
packaging = int(packaging)
if packaging == 1:
    print("plastic(500)")
    cost3 = int(500)
elif packaging == 2:
    print("bag(1000)")
    cost3 = int(1000)
elif packaging == 3:
    print("gift box(5000)")
    cost3 = int(5000)
else:
    print("enter number between 1 to 3")
location = input("enter the delivery location 1 for ktm, 2 for Lkt and 3 for Bkt")
location = int(location)
if location == 1:
    print("13% vat is added")
    tax_price = float(delivery_quantity * cost1*0.13)
    print(f"total tax amount is: {tax_price}")
    cost4 = float(tax_price)
elif location == 2:
    print("free")
    cost4 = int(0)
elif location == 3:
    print("Free")
    cost4 = int(0)
else:
    print("invalid location")
grand_total = float(cost1 * delivery_quantity + cost2 + cost3 + cost4)
print(grand_total)




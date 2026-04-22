code_item = int(input("Enter the item code: "))
quantity = int(input("Enter the quantity: "))
price = 0

if code_item == 1:
    price = 4.00
elif code_item == 2:
    price = 4.50
elif code_item == 3:
    price = 5.00
elif code_item == 4:
    price = 2.00
elif code_item == 5:
    price = 1.50
else:
    print("Product not found")

if price > 0: 
    value = quantity * price
    print(f"Total: R$ {value:.2f}")
else:
    print("Search for available item")
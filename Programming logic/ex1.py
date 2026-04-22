code1 = int(input("Enter the code for part 1: "))
quantity1 = int(input("Enter the quantity of part 1: "))
price1 = float(input("Enter the price of part 1: "))

code = int(input("Enter the code for part 2: "))
quantity2 = int(input("Enter the quantity of part 2: "))
price2 = float(input("Enter the price of part 2: "))

value = (quantity1 * price1) + (quantity2 * price2)

print(f"AMOUNT PAYABLE: R${value:.2f}")
inside = 0
outside = 0

n = int(input("Enter the integer value: "))

for i in range(n):
    a = int(input("Enter an integer number: "))
    if a >= 10 and a <= 20:
        inside += 1
    else:
        outside += 1

print(f"{inside} in")
print(f"{outside} out")
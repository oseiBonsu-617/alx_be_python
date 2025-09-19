# multiplication table

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 10):
    print(f"{number} * {i} = {number * i}")
length = int(input("Enter the size of the pattern: "))
count = 0
while count < length:
    count +=1
    for i in range(1, length+1):
        print("*", end="")
    print("\n")
num = int(input("Enter a number: "))
print("Multiples of", num, "between 1 and 100:")
for i in range(1, 101):
    if i % num == 0:
        print(i)

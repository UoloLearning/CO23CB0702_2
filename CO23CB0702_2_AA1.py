num = input("Enter a number to check if it's divisible by 5: ")
num = int(num)
remainder = num % 5
while remainder != 0:
    print(num, "is not divisible by 5.")
    num = input("Enter a new number to check: ")
    num = int(num)
    remainder = num % 5
print(num, "is divisible by 5.")

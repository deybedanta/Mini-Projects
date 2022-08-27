# WAP to print a reversed number

num = int(input("Enter your number > "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"The reversed number is {reversed_num}.")
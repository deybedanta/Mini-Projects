# WAP of a simple calculator

print ("Welcome to the calculator.")

num1 = float(input("Enter your first number > "))

num2 = float(input("Enter your second number > "))

oper = input("Choose your operator (a,s,m,d,mo,e,fd) [+,-,*,/,%,^,//] > ")

if oper.lower() == 'a':
    add = num1 + num2
    print(f"The sum is {add}.")

elif oper.lower() == 's':
    sub = num1 - num2
    print(f"The difference is {sub}.")

elif oper.lower() == 'm':
    times = num1 * num2
    print(f"The product is {times}.")

elif oper.lower() == 'd':
    quot = num1 / num2
    print(f"The quotient is {quot}.")

elif oper.lower() == 'mo':
    mod = num1 % num2
    print(f"The mod value is {mod}.")

elif oper.lower() == 'e':
    exp = num1 ** num2
    print(f"The exponentiated value is {exp}.")

elif oper.lower() == 'fd':
    fdr = num1 // num2
    print(f"The floored value is {fdr}.")

else:
    print("Error!")

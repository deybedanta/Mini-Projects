# comment

fibn = int(input("Enter number of numbers you want to be fibonacci'd > "))

a=0
b=1
i=1

print(f"The fibonacci series would be {a}, {b}, ", end="")

for i in range(2,fibn):
    c=a+b
    a=b
    b=c
    
    if i == fibn-1:
        print(c, end=".")
    else:
        print(c, end=", ")

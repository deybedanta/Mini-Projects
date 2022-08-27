# WAP to print sum of first n natural numbers

n = int(input("Enter number of natural numbers to add > "))

add = 0
for i in range(1,n+1):
  add += i
# For whole numbers we just have to change the 1 in `for i in range(1,n+1)` to 0

print(f"The sum of first {n} natural numbers is {add}.")
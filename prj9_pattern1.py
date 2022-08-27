# WAP to print the following pattern:
"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

for i in range(5, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print()

# WAP to validate leap year

year = int(input("Enter a year > "))

if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year!")

elif (year % 4 ==0) and (year % 100 != 0):
    print(year, "is a leap year!")

else:
    print(year, "isn't a leap year... (Suggestion: If you like leap years, try '2012'!)")
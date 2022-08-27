# WAP to take temps. for each day, and output average temp. for the week

print("Please input the temperature values one by one. DO NOT add units.")
print("")

sun = float(input("What was the temperature on Sunday? > "))
mon = float(input("What about Monday's temperature? > "))
tue = float(input("What was Tuesday's temperature like? > "))
wed = float(input("Tell me about Wednesday's temperature! > "))
thu = float(input("And temperature of Thursday was...? > "))
fri = float(input("We're almost there! Friday's temperature was...? > "))
sat = float(input("Finally, what was Saturday's temperature? > "))

avgtemp = sun+mon+tue+wed+thu+fri+sat/7
print("")
unit = input("What is your preferred unit? (c - Celsius / f - Fahrenheit) > ")

if unit.lower() == 'c':
    print(f"The average temperature this week was {avgtemp} degrees Celsius.")
elif unit.lower() == 'f':
    print(f"The average temperature this week was {avgtemp} degrees Fahrenheit.")
else:
    print("Illegal unit.")
# WAP to accept time in seconds and convert it to minutes and seconds

seconds = int(input("Enter your time in seconds > "))

minutes, seconds = divmod(seconds, 60)

print(f"The converted time is {minutes} minutes and {seconds} seconds.")
# 11) Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and "Good afternoon!" otherwise.
current_hour = int(input("Enter the current hour (0-23): "))
if current_hour < 12:
     print("Good morning!")
else:
     print("Good afternoon!")
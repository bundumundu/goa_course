#  3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive.
print("Even numbers:")
for num in range(101):
     if num % 2 == 0:
         print(num, end=" ")
print("Odd numbers:")
for num in range(101):
     if num % 2 != 0:
         print(num, end=" ")
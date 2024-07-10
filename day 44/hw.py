#  დავალებები :
#      For Loop:

#  1) Print all integers from 0 to 20 inclusive.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(20):
      print(number_list[i])

#  2) Print the first 10 natural numbers.
number_list = []
for i in range(11):
       number_list.append(i)
print(number_list)

#  3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive.
print("Even numbers:")
for num in range(101):
     if num % 2 == 0:
         print(num, end=" ")

print("Odd numbers:")
for num in range(101):
     if num % 2 != 0:
         print(num, end=" ")

#  4)Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).
number = int(input("Enter a number: "))
total_sum = 0
for i in range(1, number + 1):
    total_sum += i
print(f"The sum of all numbers up to {number} is {total_sum}")

#5) Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50 inclusive
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# While Loop:

# 1) Print even numbers up to 20.
number = 2 
while number <= 20:
    print(number)
    number += 2

# 2) calculate the sum of numbers from 1 to 10.
total_sum = 0
for number in range(1, 11):
     total_sum += number
print("The sum of numbers from 1 to 10 is:", total_sum)

# 3) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.
correct_number = 7
guessed_number = None
while guessed_number != correct_number:
     guessed_number = int(input("Guess a number between 1 and 10: "))
     if guessed_number != correct_number:
         print("your wrong ")
print("Congrats your right")

# 4) Write a while loop that processes a list of numbers, doubling each number, and prints the new list
numbers = [1, 2, 3, 4, 5]
index = 0
length = len(numbers)
while index < length:
    numbers[index] *= 2
    index += 1
print("Modified list after doubling each number:", numbers)

# 5) Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.
correct_password = "password123"
user_input = ""
while user_input != correct_password:
    user_input = input("Enter the password: ")
    if user_input != correct_password:
        print("Incorrect password Please try again!")
        print("Correct password . Access granted!")

 #If - Else:

# 1) Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and "Good afternoon!" otherwise.
current_hour = int(input("Enter the current hour (0-23): "))
if current_hour < 12:
     print("Good morning!")
else:
     print("Good afternoon!")

# 2) Write an if-else statement that checks if a number is even or odd. If the number is even, print "Even"; otherwise, print "Odd."
number = int(input("Enter a number: "))
if number % 2 == 0:
     print("Even")
else:
     print("Odd")

# 3) Create an if-else statement to check if the temperature is above 30 degrees. If it is, print "It's hot outside!"; otherwise, print "It's not too hot."
temperature = float(input("Enter the current temperature: "))
if temperature > 30:
     print("It's hot outside!")
else:
     print("It's not too hot.")

#4) Create an if-else statement that determines if a person is a teenager. If the age is between 13 and 19 (inclusive), print "You are a teenager!"; otherwise, print "You are not a teenager.
age = int(input("Enter your age: "))
if age >= 13 and age <= 19:
     print("You are a teenager!")
else:
    print("You are not a teenager.")
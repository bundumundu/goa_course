# 10) Write a while loop that processes a list of numbers, doubling each number, and prints the new list
numbers = [1, 2, 3, 4, 5]
index = 0
length = len(numbers)
while index < length:
    numbers[index] *= 2
    index += 1
print("Modified list after doubling each number:", numbers)

# 9) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.
correct_number = 7
guessed_number = None
while guessed_number != correct_number:
     guessed_number = int(input("Guess a number between 1 and 10: "))
     if guessed_number != correct_number:
         print("your wrong ")
print("Congrats your right")

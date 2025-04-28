# 1) ააწყვეთ ჯეირანის პროგრამა სადაც ორი მომხმარებელი ერთმანეთს ეთამაშება ჯეირანს
import random
options = ['rock', 'paper', 'scissors']
player = None
running = True
while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:   
        player = input('enter a choise (rock , paper or scissors) ')\

    print(f"player: {player}" )

    print(f"computer: {computer}" )

    if player == computer:
        print('its a tie')
    elif player == 'rock' and computer == 'scissors':
        print('you win!')
    elif player == 'paper' and computer == 'rock':
        print('you win!')
    elif player == 'scissors' and computer == 'paper':
        print('you win!')
    else:
        print("you lose!")

    if not input('play again? (y/n) ') == 'y':
       running = False

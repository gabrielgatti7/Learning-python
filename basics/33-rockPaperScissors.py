import random

choice = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(choice)

    player = input('Rock (r), paper (p), or scissors (s)?: ').lower()
    while player != 'r' and player != 'p' and player != 's':
        player = input('Rock (r), paper (p), or scissors (s)?: ').lower()

    print('Computer: '+computer)

    if (player == 'r' and computer == 'rock') or (player == 'p' and computer == 'paper') or (player == 's' and computer == 'scissors'):
        print('Draw!')
    elif (player == 'r' and computer == 'scissors') or (player == 'p' and computer == 'rock') or (player == 's' and computer == 'paper'):
        print('You win!')
    elif (player == 'p' and computer == 'scissors') or (player == 'r' and computer == 'paper') or (player == 's' and computer == 'rock'):
        print('You lose!')

    again = input('Play again? (y/n): ').lower()
    if again != 'y':
        break
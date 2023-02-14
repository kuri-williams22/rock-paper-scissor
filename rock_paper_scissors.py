# rock paper scissor game
import random

options = ['rock', 'paper', 'scissor']
user_score = 0
computer_score = 0

exit = False

print('Welcome to the Rock, Paper, Scissor game!')
print('-----------------------------------------')
while exit == False:
    user_input = input('Enter rock, paper, or scissor: ').lower()
    computer_input = random.choice(options)
    
    if user_input == 'exit':
        print('Thank you for playing.  Goodbye!')
        exit = True
    
    # if user enters rock
    if user_input == 'rock':
        if computer_input == 'rock':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('It is a tie!')
        elif computer_input == 'paper':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('Computer wins!')
            computer_score += 1
        elif computer_input == 'scissor':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('You win!')
            user_score += 1
            
    #else if user enters paper
    elif user_input == 'paper':
        if computer_input == 'paper':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('It is a tie!')
        elif computer_input == 'scissor':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('Computer wins!')
            computer_score += 1
        elif computer_input == 'rock':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('You win!')
            user_score += 1
            
    #else if user enters scissor
    elif user_input == 'scissor':
        if computer_input == 'scissor':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('It is a tie!')
        elif computer_input == 'rock':
            print(f'You entered {user_input}: Computer entered {computer_input}')
            print('Computer wins!')
            computer_score += 1
        elif computer_input == 'paper':
            print(f'You entered {user_input} : Computer entered {computer_input}')
            print('You win!')
            user_score += 1
    else:
        print('This is not a valid option.  Please enter: rock, paper, or scissor.')
    
    print(f'User score {user_score} || Computer score: {computer_score}')
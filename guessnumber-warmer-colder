from random import randint

# init vars
answer = randint(1,100)
guess = 0
guess_list = []

# main program
while guess != answer:
    
    # Player guess input
    guess = int(input('Guess [1-100]: '))

    # Check win
    if guess == answer:
        # Player wins
        print('Answer:', answer)
        print('Turns', len(guess_list))
        print('Guesses:', str(guess_list))
        exit()
        
    # OOB check
    if guess < 1 or guess > 100:
        print('Warning: Value must be between 1-100')
        continue

    # check if first turn
    if len(guess_list) == 0:
        print('First Guess')
    else:
        if abs(guess_list[-1] - answer) < abs(guess - answer):
            print('Colder')
        else:
            print('Warmer')

    # Add guess to list
    guess_list.append(guess)


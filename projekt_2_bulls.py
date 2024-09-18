"""

projekt_2_bulls.py: druhý projekt do Engeto Online Python Akademie

author: Tatiana Staronova
email: tatiana@staronova.me

"""

from random import choice
import time


# function definition 

def incorrect_length (guess, random_number) -> bool:
    """ Checks whether the user input meets 
    the length requirement."""
    return len(str(guess)) != len(str(random_number)) 

def inccorect_datatype(guess) -> bool:
    """ Checks whether the user input meets 
    the data type requirement."""
    return not str(guess).isdigit()

def starting_with_zero (guess) -> bool:
    """Tests whether user input starts with a zero."""
    return str(guess)[0] == str(0)    
    
def unique_numbers (random_number) -> bool:
    """Ensures non-repeating numbers in random guess."""
    return len(set(str(random_number))) == 4
    

# random number generator
while True:
    random_number = str(choice(range(1000, 10000)))
    if unique_numbers(random_number):
        break   

print(f'Hi there!')
print('-'*47)
print(f"I've generated a random {len(random_number)} digit number for you.")
print("Let's play a bulls and cows game.")
print('-'*47)
print('Enter a number:')
print('-'*47)


start = time.time()
number_of_attempts = 1

while True:
    # input verification
    guess = str(input().strip())
    if incorrect_length(guess, random_number):
        print(f"You need to enter {len(random_number)}-figure number, let's try again.")
        continue
    if inccorect_datatype(guess):
        print(f"Your entry needs to be a number, let's try again!")
        continue
    if starting_with_zero(guess):
        print(f"Your guess can not start with a zero, let's try again!")  
        continue
    if not unique_numbers(guess):
        print(f"Your guess must consist of unique numbers, let's try again!")
        continue

    # hladanie spravneho cisla
    print(f'>>> {guess}')
    if guess != random_number:
        bulls = 0
        cows = 0
        # cows
        for number in random_number:
            if number in guess:
                cows += 1
        # bulls
        for index in range(len(guess)):
            if guess[index] == random_number[index]:
                bulls += 1    
        cows -= bulls
        number_of_attempts += 1

    # singular/plural pre bulls/cows
        if cows == 1:
            female_animal = "cow"
        else:
            female_animal = "cows" 
        
        if bulls == 1:
            male_animal = "bull"
        else:
            male_animal = "bulls"

        print(f'{bulls} {male_animal}, {cows} {female_animal}')
        print('-'*47)
        continue
    else:
        # vypisanie vysledku
        stop = time.time()
        print(f"Correct, you've guessed the right number in {number_of_attempts} guesses!")
        print('-'*47)
        print(f"It took you {round(stop-start)} seconds.")
        if  number_of_attempts < 5:
            print("That's amazing, good job!")
        if 5< number_of_attempts < 10:
            print("That's pretty good.")
        if number_of_attempts > 10:
            print("Not bad...")
        break

"""

projekt_2_bulls.py: druhý projekt do Engeto Online Python Akademie

author: Tatiana Staronova
email: tatiana@staronova.me

"""

from random import choice
import time

# vygenerovanie nahodneho cisla
cislo = str(choice(range(1000, 10000)))

print(f'Hi there!')
print('-'*47)
print(f"I've generated a random {len(cislo)} digit number for you.")
print("Let's play a bulls and cows game.")
print('-'*47)
print('Enter a number:')
print('-'*47)

tip = str(input())

pocet_pokusov = 0

# osetrenie vstupu
while len(tip) != len (cislo) or not tip.isdigit():
    print(f"You need to enter {len(cislo)}-figure number, let's try again.")
    tip = str(input())
else:
    # hladanie spravneho cisla
    start = time.time()
    while True:
        print(f'>>> {tip}')
        if tip != cislo:
            bulls = 0
            cows = 0
            # cows
            for number in cislo:
                if number in tip:
                    cows += 1
            # bulls
            for index in range(len(tip)):
                if tip[index] == cislo[index]:
                    bulls += 1    
            cows -= bulls
            pocet_pokusov += 1

            print(f'{bulls} bulls, {cows} cows')
            print('-'*47)
            
            # dalsi pokus
            tip = str(input())

            while len(tip) != len (cislo) or not tip.isdigit():
                print(f"You need to enter {len(cislo)}-figure number, let's try again.")
                tip = str(input())

        # vypisanie vysledku
        else:
            stop = time.time()
            print(f"Correct, you've guessed the right number in {pocet_pokusov} guesses!")
            print('-'*47)
            print(f"It took you {round(stop-start)} seconds.")
            if pocet_pokusov < 5:
                print("That's amazing, good job!")
            if 5< pocet_pokusov < 10:
                print("That's pretty good.")
            if pocet_pokusov > 10:
                print("Not bad...")
            break



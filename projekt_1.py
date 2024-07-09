'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tatiana Staroňová
email: tatiana@staronova.me
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

import sys
from collections import Counter
from operator import itemgetter

username = input("Prihlasovaci jmeno:")
password = input('Heslo:')

known_users ={'bob': '123', 'ann': 'pass123', 
             'mike': 'password123','liz': 'pass123'}

print(f'username: {username}')
print(f'password: {password}')
print('-'*40)

# overenie uzivatela

while username not in known_users:
    print('unregistered user, terminating the program') 
    break
else:
    saved_pass = known_users[username]
    if saved_pass == password:
        print(f'Welcome to the app, {username}')
        print('We have 3 texts to be analyzed.')
        print('-'*40) 


# vybratie textu na analyzu

    text = input('Enter a number btw. 1 and 3 to select:')

    
    if not text.isnumeric() or int(text) not in range(1,4):
        print('Wrong entry')
        sys.exit(1)

    print(f'Enter a number btw. 1 and 3 to select: {text}')
    print('-'*40)

    text_numb = int(text)
    selected_text = TEXTS[text_numb-1]

# ocistenie textu

    clean_words = []

    for word in selected_text.split():
        clean_words.append(word.strip(',.'))

# statistika

    word_count = len(clean_words)
    print(f'There are {word_count} words in selected text.')

    starts_upper = 0    
    all_upper = 0
    all_lower = 0
    numbers = []
    for word in clean_words:
        if word.isupper():
            all_upper += 1
        elif word.islower():
            all_lower += 1
        elif word.istitle():
            starts_upper += 1
        elif word.isnumeric():
            numbers.append(int(word))
    print(f'There are {starts_upper} titlacase words.')
    print(f'There are {all_upper} uppercase words.')
    print(f'There are {all_lower} lowercase words.')
    print(f'There are {len(numbers)} numeric strings.')

    summ = sum(numbers)
    print(f'The sum of all numbers {summ}.')

# histogram

    word_lenght = Counter(len(words) for words in (clean_words))
    sorted_word_lenght = sorted(word_lenght.items())

    maximum = max(sorted_word_lenght, key = itemgetter(1))[1]

    print('-'*40)
    print(f'LEN| {"OCCURENCES".center(maximum)} |NR.')
    print('-'*40)

    for i in sorted_word_lenght:
        a = i[0]
        b = i[1]
        print(f'{a:>2} | {b*"*":<{maximum}} | {b}')
    
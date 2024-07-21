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
import string

username = input("Prihlasovaci jmeno:")
known_users ={'bob': '123', 'ann': 'pass123', 
             'mike': 'password123','liz': 'pass123'}

print('-'*40)

# overenie uzivatela

if username not in known_users:
    print('Unregistered user, terminating the program')
    sys.exit(1)

# overenie hesla

password = input('Heslo:')
saved_pass = known_users[username]
if saved_pass == password:
    print(f'Welcome to the app, {username}')
    print(f'We have {len(TEXTS)} texts to be analyzed.')
    print('-'*40) 
else:
    print('Incorrect password, terminating the program')
    sys.exit(2)


# vybratie textu na analyzu

text = input(f'Enter a number btw. 1 and {len(TEXTS)} to select:')


if not text.isnumeric() or int(text) not in range(1,len(TEXTS)+1):
    print('Wrong entry')
    sys.exit(3)

print('-'*40)

selected_text = TEXTS[int(text)-1]

# ocistenie textu

clean_words = [word.strip(string.punctuation) for word in selected_text.split()]


# statistika

word_count = len(clean_words)
print(f'There are {word_count} words in selected text.')

starts_upper = 0    
all_upper = 0
all_lower = 0
numbers = []
for word in clean_words:
    if word.isalpha():
        if word.isupper():
            all_upper += 1
        if word.islower():
            all_lower += 1
        if word[0].isupper():
            starts_upper += 1
    elif word.isnumeric():
        numbers.append(int(word))
print(f'There are {starts_upper} titlecase words.')
print(f'There are {all_upper} uppercase words.')
print(f'There are {all_lower} lowercase words.')
print(f'There are {len(numbers)} numeric strings.')
print(f'The sum of all numbers {sum(numbers)}.')

# histogram

word_length = Counter(len(words) for words in (clean_words))
sorted_word_length = sorted(word_length.items())

maximum = max(sorted_word_length, key = itemgetter(1))[1]

print('-'*40)
print(f'LEN| {"OCCURENCES".center(maximum)} |NR.')
print('-'*40)

for i in sorted_word_length:
    a = i[0]
    b = i[1]
    print(f'{a:>2} | {b*"*":<{maximum}} | {b}')
    
"""
projekt_1.py: první projekt do Engeto Oline Python Akademie

author: Zdeněk Brabec
email: brabecz57@gmail.con
"""

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

# Vytvoření slovníku uživatelů a jejich hesel

reg_users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}
# Zadání přihlašovacích údajů

user = input("Enter your username: ")
password = input("Enter your passeord: ")
print("-"*40)

# Kontrola uživatelského jména a hesla

if user in reg_users and reg_users[user] == password:
    print("Welcome to the app,", user)
    print("we have 3 texts to be analyzed.")
    print("-"*40)
else:
    print("unregistered user, terminating the program..")
    exit()

# Výběr textu k analýze

choice_text = int(input("Enter a number btw. 1 and 3 to select: "))
if choice_text < 1 or choice_text > 3:
    print("Invalid choice. Exiting.")
    exit()

selected_text = TEXTS[choice_text - 1]
print("-"*40)

# Analýza textu

words = selected_text.split()
words_count = len(words)
titlecase_words = sum(1 for word in words if word.istitle())
uppercase_words = sum(1 for word in words if word.isupper()and word.isalpha())
lowercase_words = sum(1 for word in words if word.islower())
numeric_strings = [int(word) for word in words if word.isdigit()]
numeric_count = len(numeric_strings)
numeric_sum = sum(numeric_strings)

# Výpis z analýzy textu

print("There are", words_count, "words in the selected text.")
print("There are", titlecase_words, "titlecase words.")
print("There are", uppercase_words, "uppercase words.")
print("There are", lowercase_words, "lowercase words.")
print("There are", numeric_count, "numeric strings.")
print("The sum of all the numbers", numeric_sum)
print("-"*40)

# Četnost délek slov

word_lengths = {}
for word in words:
    length = len(word.strip(",.!?"))
    word_lengths[length] = word_lengths.get(length, 0) + 1

# Zobrazení grafu

print("LEN|  OCCURRENCES  |NR.")
print("-"*40)
for length in sorted(word_lengths):
    occurrences = word_lengths[length]
    print(f"{length:>3}|{'*' * occurrences:<15}|{occurrences}")

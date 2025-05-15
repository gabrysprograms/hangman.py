import random

words = [
    "apple",
    "banana",
    "mango",
    "trawberry",
    "orange",
    "grape",
    "pineapple",
    "apricot",
    "lemon",
    "coconut",
    "watermelon",
    "cherry",
    "papaya",
    "berry",
    "peach",
    "lychee",
    "muskmelon",
]

hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """,
]


answer = random.choice(words)
max_tries = 7
wrong_guesses = 0
right_letters = set()
wrong_letters = set()

while wrong_guesses < max_tries:
    failed = 0
    print(hangman_stages[wrong_guesses])
    for char in answer:
        if char in right_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\nWygrales")
        print("Poprawne Slowo", answer)
        break

    print("\nniepoprawne litery: ", " ".join(sorted(wrong_letters)))
    print("Pozostala ilosc prob: ", max_tries - wrong_guesses)

    while True:
        guess = input("Podaj Litere: ").lower()
        if guess in wrong_letters or guess in right_letters:
            print("Juz uzyles tej litery, sproboj innej!")
        elif len(guess) != 1:
            print("Podaj tylko jedną litere!")
        elif not guess.isalpha():
            if guess.isdigit():
                print("Cyfra nie jest poprawną próbą!")
            else:
                print("Znak specjalny nie jest poprawną próbą!")
        else:
            break
        print("\n")
    if guess not in answer:
        wrong_letters.add(guess)
        wrong_guesses += 1
    else:
        right_letters.add(guess)

if wrong_guesses == max_tries:
    print("\nNiestety, przegrałeś!")
    print("Poprawne słowo to:", answer)

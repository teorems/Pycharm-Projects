# Write your code here
import random
print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit:')
    print()
    if menu == "play":
        pass
    elif menu == "exit":
        break
    else:
        print("You should type 'play' or 'exit'.")
        print()
        continue
    words = ['python', 'java', 'kotlin', 'javascript']
    word = list(random.choice(words))
    word_copy = list("-" * len(word))
    tries = 0
    guesses_done = set()
    while tries < 8:
        print("".join(word_copy))
        if word_copy == word:
            print("You guessed the word!")
            print("You survived!")
            print()
            break
        guess = input("Input a letter:")
        if not len(guess) == 1:
            print("You should input a single letter.")
            print()
            continue
        if not guess.isalpha() or not guess.islower():
            print("It is not an ASCII lowercase letter.")
            print()
            continue
        if guess in guesses_done:
            print("You already typed this letter")
            print()
            continue
        if guess in word:
            for index, letter in enumerate(word, 0):
                if letter == guess:
                    word_copy[index] = guess
            print()
        else:
            print("No such letter in the word")
            tries += 1
            if tries == 8:
                print("You are hanged!")
            print()
        guesses_done.add(guess)

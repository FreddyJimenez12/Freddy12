import random

word = ['death', 'math', 'homework', 'money', 'games', 'stuff', 'Family', 'school', 'Edison', 'Gaston']
guesses = 10
random_word = random.choice(word)
listOne = list(random_word)
letter_used = []
playing = True

print("let's play a game of hangman")
print("you're going to have 10 guess to guess the word.")
while guesses > 0 and playing:
    # Create and update display
    display = []
    for letter in random_word:
        if letter.lower() in letter_used:
            display.append(letter)
        else:
            display.append("*")
    print(''.join(display))
    print(guesses)

    # Check for win
    if '*' not in display:
        print("you win the word was %s" % random_word)
        playing = False
        continue

    # Ask for input and add it to letters used
    guess = input("letter :").lower()
    letter_used.append(guess)
    print(letter_used)

    if guess == random_word.lower():
        print("you win the word was %s" % random_word)
        playing = False
        continue

    # Check for loss
    if guess not in random_word:
        guesses -= 1
        if guesses == 0:
            print("you lost the word was %s" % random_word)

            # print(guess)
            # for guess in range(len(word)):
            #     if guess != strOne in string.ascii_letters:
            #         print("guess again")
            #     else:
            #         print("you found a letter")
            #         print(display.append(guess))
            # if guess == word in listOne:
            #     print(display)

"""


    # if stuff in listTwo:
    #     if stuff != listTwo in word:
    #         print(guess - 1)


    # listTwo[i] = guess
    # guess.append = listTwo[i]

        if guess not in random_word:
        guesses -= 1
    for letter in random_word:
        if letter in guess:
            display = guess
        else:
            listOne.append('*')
    letter_used = '*'.join(letter_used)
    if '*' not in display:
        print("you win the word was %s" % random_word)
        break


"""
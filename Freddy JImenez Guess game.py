import random


# while number < 10:
#     guess = input()
#     guess = int(guess)
#
# if number < guess:
#    print("it's low")
# input(">_")
# guess = input
# num = 'import random'
#

# def print (num):
#    if guess == num():
#     return print("correct")
#   elif guess < num:
#     return print("go higher")
#   elif guess > num:
#     return print("go lower")


# def number(guess_num):
#    if guess == num:
#     print("correct")
#    elif str(guess) < num:
#     print("higher")
#    elif str(guess) < num :
#     print("lower")


        # generate a number, ask the user for an input(number), does the guess match the number?  #  add "higher" or "lower" , add 5 guesses

guessTaken = 0

number = random.randint(1, 50)


while guessTaken < 5:
    print("take a guess")
    guess = int(input())

    guessTaken = guessTaken + 1

    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        print("correct")

    if guess != number:
        number = str(number)
        print("Nope. The number I was thinking of was " + number)
        # generate a number, ask the user for an input(number), does the guess match the number?  #  add "higher" or "lower" , add 5 guesses
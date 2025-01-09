import random
number = 0
money = 15
win = 7
print("so do you want to play a game of lucky 7")
print("you start off with $15 just spend a $1 to gamble your money to play this game.")
while money > 0:
    D1 = (random.randint(1, 6))
    D2 = (random.randint(1, 6))
    stuff = int(input())
    money -= 1
    number = number + 1
    print(D1)
    print(D2)
    print(D1 + D2)
    if (D1 + D2) == win:
        print("you win here 4 dollars, want to play again")
        print(" your money is")
        money += 5
        print("money =", money)
    elif (D1 + D2) != win:
        print("you lost want to play again, just insert $1")
        print("money =", money)
    if money == number:
        print("the amount of round you played")
        print("round =", number)
        print("also the money you earn")
        print("money =", money)








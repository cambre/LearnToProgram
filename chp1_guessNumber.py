# Chapter 1
# Includes random number from 1-10.
# Runs on loop until guess is correct.
__author__ = 'Cambre'
from random import randint
secret = randint(1,10)
print("Welcome")
guess = 0
while guess != secret:
    g = input("Guess the number from 1 to 10: ")
    guess = int(g)
    if guess == secret:
        print ("You win!!!")
    else:
        if guess > secret:
            print ("Too high")
        else:
            print ("Too low!")
print ("Game over!")
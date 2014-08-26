# Chapter 1
__author__ = 'Cambre'
print("Welcome")
g = input("Guess the number: ")
guess = int(g)
if guess ==5:
    print ("You win!")
else:
    if guess < 5:
        print ("Too low!")
    else:
        print ("Too high!")
print ("Game over!")
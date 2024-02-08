import random

ans = random.randint(1,100)
chance = 7

while chance != 0:
    guess = int(input("Input the guess number : "))
    chance -= 1
    if guess == ans:
        print(f"That's correct. Random number is {ans}!!")
        break
    elif guess < ans:
        print(f"The number is greater than {guess}.")
    else:
        print(f"The number is lower than {guess}.")
else:
    print("You've exhausted our chances of guessing. Random number is {ans}!!")
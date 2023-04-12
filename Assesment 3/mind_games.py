# Importing required libraries
import random

# Initializing variables and arrays
limit = 10
count = 99
answer = 0
rand = 0
arr = []

# Displaying the game instructions
print("           MIND GAMES\n")
print("1. Think of a number between 10 - 99")
print("2. Add the two numbers for example:'you choose 15 so 1+5 = 6'")
print("3. Turn the sum of the numbers into subtraction numbers")
print("4. Concentrate your mind on the character of your number\n")

# Generating a random ASCII character between '!' and 'o'
answer = chr(random.randint(33, 111))

# Generating the characters to be displayed and generating the answer
for b in range(limit):
    for k in range(limit):
        count -= 1
        if count < 9:
            rand = chr(random.randint(33, 111))
            if (count+1) % 9 == 0:
                print(" %d=%c " % (count+1, answer), end="")
            else:
                print(" %d=%c " % (count+1, rand), end="")
        else:
            rand = chr(random.randint(33, 111))
            if (count+1) % 9 == 0:
                print("%d=%c " % (count+1, answer), end="")
            else:
                print("%d=%c " % (count+1, rand), end="")
    print()

# Prompting the user to press Enter to reveal the character they were thinking of
print("\nEach number above represents a character")
input("Press Enter to see the character of the number you are thinking of !!!")

# Displaying the character the user was thinking of
print("\nThe character you think of %c" % answer)
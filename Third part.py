import random
import sys

number = random.randint(1, 10)
print("Привіт! Тобі треба вгадати яке число я загадав. У тебе 3 спроби.")
for i in range(3):
    guess = int(input(f"Cпроба {i+1}: "))
    if guess == number:
        print("Ти виграв!")
        sys.exit()
##Про sys мені розповів чат гпт бо я не знав як примусово зупити програму, break не працював.##
    elif guess > number:
        print("Меньше.")
    elif guess < number:
        print("Більше.")
print("Ти програв!")
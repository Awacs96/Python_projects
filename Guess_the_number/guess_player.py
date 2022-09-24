# Player has to guess the number
import random

while True:
    try:
        upper_range = int(input("Chose the upper range of the guessing range: "))
        break
    except:
        print("Please enter a valid integer.")

attempt = 0
secret_number = random.randint(1, upper_range)

guess = 0
previous = []

while guess != secret_number:
    attempt += 1

    while True:

        try:
            guess = int(input("What is your guess?\n"))
            break
        except:
            print("Please enter a valid integer.")
        
    if guess in previous:
        print(f"You have tried this number before.")
        attempt -= 1
    else:
        previous.append(guess)

print(f"Congratulations, you guessed the secret number ({secret_number}) on {attempt} attempt.")
# Computer guesses the number. You are calling the function with a parameter = the upper value (the range starts with 1)
# Parameter "remembers" is there to potentially improve the PC result - we then create a list of already generated tips

import random

def pc_guesser(upper_limit, remembers=True):
    guesses = 1
    memory = []
    rand = random.randint(1, upper_limit)
    pc_tip = random.randint(1, upper_limit)

    while pc_tip != rand:
        guesses += 1
        print(memory, pc_tip)

        if remembers == True:
            memory.append(pc_tip)

            while pc_tip in memory:
                pc_tip = random.randint(1, upper_limit)
        else:
            pc_tip = random.randint(1, upper_limit)
        
        print("End loop guess: ", pc_tip)

    print(f"The computer hit the correct number after {guesses} guesses. The number was: {rand}.")

pc_guesser(10)
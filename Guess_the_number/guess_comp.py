# Computer guesses the number. You are calling the function with a parameter = the upper value (the range starts with 1)
# Parameter "remembers" is there to potentially improve the PC result - we then create a list of already generated tips

import random

def makeTip(upper):
    return random.randint(1, upper)

def pc_guesser(upper_limit, remembers=True):
    guesses = 0
    memory = []
    rand = random.randint(1, upper_limit)
    pc_tip = random.randint(1, upper_limit)

    while pc_tip != rand:

        print(pc_tip)

        if remembers == False:
            pc_tip = makeTip(upper_limit)
            guesses += 1
            continue
        else:
            if pc_tip not in memory:
                memory.append(pc_tip)
                pc_tip = makeTip(upper_limit)
                guesses += 1
            else:
                while pc_tip in memory:
                    pc_tip = makeTip(upper_limit)
                continue

    
    print(f"The computer hit the correct number after {pc_tip} guesses. The number was: {rand}.")


pc_guesser(10)
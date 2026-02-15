import random
failure = 0
success = 0
while True:
    roll = random.randint(1,20)
    if roll == 1:
        failure += 2
    elif roll < 10:
        failure += 1
    elif roll == 20:
        print("Gain 1 health and have revived")
        break
    else: success += 1
    
    if failure >= 3:
        print("Die")
        break
    if success >= 3:
        print("Stable but unconscious")
        break
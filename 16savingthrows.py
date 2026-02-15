import random
def dc(dc):
    roll = random.randint(1,20)
    return roll >= dc
print(dc(5), dc(10), dc(15))
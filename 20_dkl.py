import math

def dkl(list1, list2):
    dkl = 0
    if len(list1) == len(list2):
        for p, q in zip(list1, list2):
            if q <= 0:
                print("cannot calculate")
                break
            else: dkl += p * math.log2(p/q)
    return dkl

p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))
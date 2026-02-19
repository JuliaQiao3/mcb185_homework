import math
import sys

probs = []
for arg in sys.argv[1:]:
    f = float(arg)
    if f <= 0 or f >= 1: sys.exit("error: not a probability")
    probs.append(float(arg))

total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):
    sys.exit("error: probs must sum to 1.0")

def entropy(list):
    H = 0
    for val in list:
        H += val * math.log2(val)
    H *= -1
    return H

print(f'{entropy(probs):.4f}')

# a = [0.5,0.25,0.15,0.1]
# print(entropy(a))
import math

def char_to_prob(s):
    if len(s) != 1:
        return None
    Q = ord(s) - 33
    error = 10**(-Q/10)
    return error

def prob_to_char(a):
    if not (0 < a < 1):
        return None
    Q = -10 * math.log10(a)
    if Q < 0 or Q > 93:
        return None
    s = chr(round(Q + 33))
    return s

print(char_to_prob('A'))
print(prob_to_char(0.001))
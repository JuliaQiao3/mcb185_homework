for a in range(1, 100):
    for b in range(a+1, 100):
        c = (a**2 + b**2)**0.5
        if c % 1 == 0:
            print(a, b, int(c))

"""
a = 3
b = 3
for j in range(51):
    for i in range(100):
        b += 1
        if a + b >= 100:
            break
        c = (a**2 + b**2)**0.5
        if c % 1 ==0 and a < b:
            print(a, b, int(c)) 
    a += 1
    b = a
"""
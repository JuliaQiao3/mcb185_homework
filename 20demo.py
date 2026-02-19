
import sys
print(sys.argv)

x = float('hello')


'''
line = input('type something and hit return: ')  
print('that line was', len(line), 'characters long')  
print(len("hello world!"))

items = list()
print(items)
items.append("eggs")
print(items)

alph = 'ACDEFGHIKLMPQRSVW'
print("index G?", alph.find("G"))
print("index Z?", alph.find("Z"))

print(alph)
aas = list(alph)
print(aas)
s = "-".join(aas)
print(s)
s = "".join(aas)
print(s)

text = 'good day          to you'
words = text.split()
print(words)

nts = ["A", "T", "C"]
print(nts)
nts[2] = "G"
print(nts)

nt = [1,2,3,4.5]
nt = nts.copy()
nt.sort()
print(nt)
nt.sort(reverse=True)
print(nt)
print(nts)

nts = "ACGT"
names = ('adenine', 'cytosine', "guanine", "thymine")
for i, nt in enumerate(nts):
    print(i, nt)
for nt, name in zip(nts, names):
    print(nt, name)
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

tax = ("Homo", 'sapiens', 9606)
print(tax[0])
print(tax[::-1])

s = 'ABCDEFGHIJ'
print(s, s[::], s[::1], s[::-1])

for i in range(len(seq)):
    print(i, seq[i])


for nt in seq:
    print(nt, end='')
print()

for nt in seq:
    print(nt, end='')

for nt in seq:
    print(nt)
print()

for nt in seq:
    print(nt)


s1 = 'hey "dude"'  
s2 = "don't tell me what to do"  
print(s1, s2)

s = "Hello world!!!"
print(s.replace('o', ''))  
print(s.replace('o', '').replace('z', 'i'))

import math
print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify
'''
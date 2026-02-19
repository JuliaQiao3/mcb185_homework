import sys

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

s = "  ".join(alphabet)
print("   " + s)
for i in alphabet:
    row = i
    for j in alphabet:
        if i == j:
            row += " " + match
        else:
            row += " " + mismatch
    print(row)

'''
# alph = list(alphabet)  # can iterate directly over characters
s = "  ".join(alphabet)
print("   " + s)
for i in range(0, len(alph)):
    check = alph[i]
    for j in range(0, len(alph)):
        if alph[i] == alph[j]:
            check += " " + match
        else:
            check += " " + mismatch
    print(check)
'''

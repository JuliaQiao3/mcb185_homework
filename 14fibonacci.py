pre1 = 0
pre2 = 1

print(pre1)
print(pre2)

for i in range(8):
    now = pre1 + pre2
    print(now)
    pre1 = pre2
    pre2 = now

"""
now = 0
pre1 = 0
pre2 = 0
for i in range(10):
    pre2 = pre1
    pre1 = now
    if i == 1:
        now = 1
    else: now = pre2 + pre1
    print (now)
"""
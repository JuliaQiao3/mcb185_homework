import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0
for trial in range(trials):
    list = []
    for k in range(people):
        list.append(random.randint(0, days-1))
    found = False
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                same += 1
                found = True
                break
        if found:
            break

prob = same / trials
print(prob)
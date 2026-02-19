import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0
for trial in range(trials):
    calendar = []
    for k in range(days):
        calendar.append(0)
    for i in range(people):
        birth = random.randint(0,days-1)
        calendar[birth] += 1
    calendar.sort(reverse = True)
    if calendar[0] >= 2:
        same += 1

prob = same / trials
print(prob)
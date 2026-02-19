import sys

# making list
list = []
for arg in sys.argv[1:]:
    list.append(float(arg))
list.sort()

# The number of values
len = len(list)
print("The number of values is", len)

# The minimum and maximum values
# The mean 
min = list[0]
max = list[-1]
sum = 0
for val in list:
    sum += val
mean = sum / len

print("The minimum values is", min)
print("The maximum values is", max)
print("The mean is", mean)

# standard deviation
sd = 0
for val in list:
    sd += (val - mean)**2
sd = (sd / len)** 0.5
print("The standard deviation is", sd)

# The median value
if len % 2 == 1:
    median = list[len // 2] # start from 0
else:
    med1 = list[len // 2 -1]
    med2 = list[len // 2]
    median = (med1 + med2)/2
print('The median value is', median)
def mean(list):
    sum = 0
    for val in list:
        sum += val
    mean = sum/len(list)
    return mean

# a = [1,2,3,20004,100,9,10,-1]
# print(mean(a))
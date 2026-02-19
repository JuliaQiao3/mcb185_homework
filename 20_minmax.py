def minmax(list):
    min = list[0]
    max = list[0]
    for val in list:
        if min < val: min = val
        if max > val: max = val
    return min, max

# a = [1,2,3,4,100,9,10,-1]
# print(minmax(a))

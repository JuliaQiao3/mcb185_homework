def minimum(list):
    min = None
    for i, num in enumerate(list):
        if min == None or num < min:
            min = num
    return min

# a = [1,2,3,4,100,9,10,-1]
# print(minimum(a))

'''
def minimum(vals):
    mini = vals[0]
    for val in vals[1:]:
        if val < mini : mini = val
    return mini
'''
def average(l):
    sum = 0
    for x in l:
        sum = sum + x
    n = len(l)
    return sum/x
l = [1,2,3,4,6,7,8,5,4,33,2,2,2,3,4,5,6]
print(average(l))

def average2(p):
    return sum(p)/len(p)
p = [1,2,3,4,5,6,7,6,5,4,3,69,2,1,2,4]
print(average2(p))


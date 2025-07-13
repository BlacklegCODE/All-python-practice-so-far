def check(l):
    small = []


    for i in l:
        if x >= i:
            small.append(i)
    return small


l = [1,2,3,4,5,55,66,77,8,88,99,99]
x = 10
get = check(l)

print(get)

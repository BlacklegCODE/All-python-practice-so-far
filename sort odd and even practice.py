def oddneven (l):
    even= []
    odd = []
    for x in l:
        if x / 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    return even,odd

l = [1,2,3,4,5,6,7]

even,odd = oddneven(l)
print( even)
print(odd)
print(oddneven(l))

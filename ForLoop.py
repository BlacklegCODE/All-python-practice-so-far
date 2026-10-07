#for loop
marks = [34,43,55,67,87,99]
a = 1
for i in marks:
    if i == 55:
        a +=1
        print("Found at index :",a)
        break;

#set functions
a = {1,2,3,4,5,6,7}
b = {5,4,3,7,8,6,2}

print(a | b)
print( a & b)
print(a - b)



import collections

d1 = {'a':1 , 'b' :2}
d2 = {'c':3,'d':4}
d3 = {'e':5,'f':6}

c = collections.ChainMap(d1,d2)

new = c.new_child(d3)
print(new)
print(c)

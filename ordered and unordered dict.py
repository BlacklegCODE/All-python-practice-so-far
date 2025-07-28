from collections import OrderedDict

#below is ordered dict practice


d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

d.pop('a')
d['a'] = 3
for key, value in d.items():
    print(key, value)

print()
print()

#below is unordered dict practice


dd = {}
dd['a'] = 1
dd['b'] = 2
dd['c'] = 3
dd['d'] = 4


dd['a'] = 6

for key, value in dd.items():
    print(key, value)

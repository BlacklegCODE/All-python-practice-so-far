from collections import namedtuple

Players = namedtuple('Boy',['name','game','level'])

x = Players('shroud','weebPUBG','god')

print(x[0])
print(x.level)

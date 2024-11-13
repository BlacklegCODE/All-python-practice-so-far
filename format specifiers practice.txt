#format specifiers :

p1 = 4400.44
p2 = 4500.789
p3 = -44.3423

print(f"First price :{p1:.2f}")
print(f"Second price:{p2:.2f}")
print(f"Third price :{p3:.2f}")
print("----------------------------------")
print(f"First price :{p1:<}")
print(f"Second price:{p2:<}")
print(f"Third price :{p3:<}")
print("----------------------------------")
print(f"First price :{p1:10}")
print(f"Second price:{p2:10}")
print(f"Third price :{p3:5}")
print("----------------------------------")
print(f"First price :{p1:>}")
print(f"Second price:{p2:>}")
print(f"Third price :{p3:>}")
print("----------------------------------")
print(f"First price :{p1:^}")
print(f"Second price:{p2:^}")
print(f"Third price :{p3:^}")
print("----------------------------------")
print(f"First price :{p1:+}")
print(f"Second price :{p2:+}")
print(f"Third price :{p3:+}")
print("----------------------------------")
print(f"First price :{p1:,}")
print(f"Second price :{p2:,}")
print(f"Third price :{p3:,}")
print("----------------------------------")

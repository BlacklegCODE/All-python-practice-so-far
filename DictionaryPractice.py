#dictionary

new_dict = {
    1:"Banana",
    2:"Apple",
    3:"Cherry",
    "fruit":"Raspberry"
}
print(new_dict)
new_dict["Name"] = "Brook"
new_dict["Random"] = "45.67"

i = 1
if 3 in new_dict:
    i+=1
    print("Found it ")
    
del new_dict[2]
print(new_dict)

for i,j in new_dict.items():
    print(i, end = "->")
    print(j)




#string indexing topic :
number = "123-123-123-123-45-674"

print(number[0])
print(number[0:5])
print(number[:6])
print(number[4:])
print(number[5:9])

# this adds steps

print(number[::2])
x = number[-4:]
print(f"The card last four digits are XXXX-XXXX-XXXX-{x}")

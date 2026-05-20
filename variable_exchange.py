a = 10
b = 20

print(f"before exchange: a = {a}, b = {b}")

# exchange
temp = a # store the value of a in temp
a = b # assign the value of b to a
b = temp # assign the value of temp (original a) to b

print(f"after exchange: a = {a}, b = {b}")


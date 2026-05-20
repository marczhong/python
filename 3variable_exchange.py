a, b, c = 100,200,300

print(f"before exchange: a = {a}, b = {b}, c = {c}")

# exchange
temp = a # store the value of a in temp
a = c # assign the value of b to a
c = b # assign the value of c to b
b = temp # assign the value of temp (original a) to c

print(f"after exchange: a = {a}, b = {b}, c = {c}")

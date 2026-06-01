# length = 1
# width = 9
# fac1 = 1
# asw = 0
# sp1 = ("   ")
# sp2 = ("  ")

# for x in range(width):
#    for y in range(length):
#       asw = fac1 * length
#       if asw < 10:
#          print(f"{fac1} x {length} = {asw}", end = f"{sp1}")
#       else:
#          print(f"{fac1} x {length} = {asw}", end = f"{sp2}")
#       fac1 += 1
#    fac1 = 1
#    length += 1
#    print()

width = 9

for row in range(1, width + 1): # row = 1, 2, 3, 4, 5, 6, 7, 8, 9
    for col in range(1, row + 1): # col = 1, 2, 3, 4, 5, 6, 7, 8, 9
        print(f"{col} x {row} = {col * row}", end="\t") # \t is used to add a tab space between the columns
    print() 

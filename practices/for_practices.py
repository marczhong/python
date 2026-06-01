# side = int(input("side"))

# for row in range(1, side + 1):
#    for column in range(row):
#       print("*", end =" ")
#    print()



# num = int(input("num"))

# for row in range(1, num + 1):
#    for col in range(1, row + 1):
#       print(col, end = " ")
#    print()

   
block = int(input("how many block?"))

for row in range(block): # Lenth
   for col in range(block): # Width
      if (col + row) % 2 == 0:
         print("⬛", end ="  ")
      else:
         print("⬜", end ="  ")
   print()
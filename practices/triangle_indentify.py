lengh1 = int(input("Enter the first lengh"))
lengh2 = int(input("Enter the second lengh"))
lengh3 = int(input("Enter the third lengh"))

if (lengh1 + lengh2 > lengh3) and (lengh1 + lengh3 > lengh2) and (lengh3 + lengh2 > lengh1):
   if (lengh1 == lengh2 == lengh3):
      print("Equilateral triangle")
   elif (lengh1 == lengh2) or (lengh1 == lengh3) or (lengh2 == lengh3):
      print("Isosceles triangle")
   else:
      print("Normal triangle")
else:
   print("Can't be a triangle")

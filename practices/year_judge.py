year = int(input("Type a year: "))


# if year % 100 == 0:
#    if year % 400 == 0:
#       print("Leap year")
#    else:
#       print("Normal year")
# else:
#    if year % 4 == 0:
#       print("Leap year")
#    else:
#       print("Normal year")


# if year % 100 != 0 and year % 4 == 0:
#    print("Leap year")
# else:
#    if year % 100 == 0 and year % 400 == 0:
#       print("Leap year")
#    else:
#       print("Normal year")
   
   
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
   print("Leap year")
else:
   print("Normal year")

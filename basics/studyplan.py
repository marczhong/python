subject = input("What subject you going to study? ")
ddl = input("whats your ddl? ")
important = int(input("Important level? (1-5)"))

print("\n== study plan ==")
print("Subject: ", subject)
print("Deadline: ", ddl)
print("Important level: ")

if important >= 4:
   print("high important")
if important == 3:
   print("medium important")
if important <= 2:
   print("low important")


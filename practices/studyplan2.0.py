student = {
   "name": input("what is your name"),
   "major": input("what is your major"),
}

tasks = []
tasks.append(input("task1?"))
tasks.append(input("task2?"))
tasks.append(input("task3?"))


importance = int(input("important level(1-5)"))

print("\n=== study plan ===")
print(f"student: {student['name']}")
print(f"major: {student['major']}\n")

print("today's tasks:")

print(tasks[0])
print(tasks[1])
print(tasks[2])

if importance >= 4:
   print("\nPriority: HIGH")

elif importance == 3:
   print("\nPriority: MEDIUM")

else:
   print("\nPriority: LOW")
   

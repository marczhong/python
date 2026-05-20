# 1
score = int(input("Type your score"))

if score >= 85:
   print("A")
elif score >= 60:
   print("B")
else:
   print("failed")


# 2
price = int(input("How much altogether"))

if price >= 500:
   print(f"{price} 20% off =", price * 0.8)
elif 300 <= price < 500:
   print(f"{price} 10% off =", price * 0.9)
elif 100 <= price <= 300:
   print(f"{price} 5% off =", price * 0.95)
else:
   print(f"no discount = {price}")


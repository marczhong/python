kw = int(input('''
How many kilowatt-hours of electricity were used?
#1  under       2880kw         , Y0.4883
#2  between     2880kw - 4800kw, Y0.5383
#3  more than   4800kw,        , Y0.7883
'''))

if kw < 0:
   print("Incorrect input")
elif kw <= 2880:
   print(f"used {kw}kw, price =", kw * 0.4883)
elif kw <= 4800:
   print(f"used {kw}kw, price =", kw * 0.5383)
else:
   print(f"used {kw}kw, price =", kw * 0.7883)

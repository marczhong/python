create_login = "admin"
create_password = "666888"

create_login2 = "root"
create_password2 = "547527"

create_login3 = "zhangsan"
create_password3 = "123456"

login = input("Type your login")
password = input("Type your password")

if login == create_login and create_password == password:
   print("Correct")
elif login == create_login2 and create_password2 == password:
   print("Correct")
elif login == create_login3 and create_password3 == password:
   print("Correct")
else:
   print("Wrong")



# by using [list]

# users = [
#    ["admin", "666888"],
#    ["root", "547527"],
#    ["zhangsan", "123456"]
# ]

# login = input("Type your login")
# password = input("Type your password")

# if [login, password] in users:
#    print("Correct")
# else:
#    print("Wrong")


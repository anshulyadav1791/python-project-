user = {"admin": "1234"}

u = input("Username: ")
p = input("Password: ")

if user.get(u) == p:
    print("Login Successful")
else:
    print("Inviled Login")

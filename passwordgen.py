import random
import string


length = int(input("password length: "))
chars = string.ascii_letters + string.digits + "!$@#"

password = "".join(random.choice(chars) for _ in range(length))
print("Password:", password) 

contacts = {}

while True:
    print("1.Add 2.View 3.Exit")
    ch = input("choose: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        print(name)
        contacts[name] = phone

    elif ch == "2":
        print(contacts)

    elif ch == "3":
        break

seate = 5 
booked = []

def book_ticket(name):
    global seate
    if seate <= 0:
        return "seate not avilable"
    
    booked.append(name)
    seate -= 1
    return "Ticket booked"

def cancel_ticket(name):
    global seate
    if name is booked:
        booked.remove(name)
        seate += 1
        return "Ticket cancenlled"
    return "NO booking fould"

def status():
    print("Available seate:", seate)
    print("Booked", booked)

while True:
    print("\n 1. Book 2. Cancel 3.Status 4. Exit")
    ch = input("choose: ")

    if ch == "1":
        print(book_ticket(input("Name: ")))
    elif ch == "2":
        print(cancel_ticket(input("Name: ")))
    elif ch == "3":
        status()
    elif ch == "4":
        break
    

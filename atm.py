balance = 10000
pin = "1234"

def check_balance():
    print(f"\n Your current balance is:💵 {balance}")

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: 💵 "))
    if amount > 0:
        balance += amount
        print(f"✅ {amount} deposited successfully")
    else:
        print("❌ Invalid amount")

def withdrow():
    global balance
    amount = int(input("Enter amount to withdrow: "))
    if amount > balance:
        print("❌ Insufficient balance")
    elif amount <= 0:
        print("❌ Invalid amount")
    else:
        balance -= amount
        print(f"✅ {amount} withdrawn successfully")


# Login .........

entered_pin = input("Enter your ATM PIN: ")

if entered_pin == pin:
    print("\n ✅ Login successful")

    while True:
        print("\n------ ATM MENU ------")
        print("1. Chack Balance")
        print("2. Deposit Money")
        print("3. Withdrow Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdrow()
        elif choice == "4":
            print("🙏 Thank you for using ATM")
            break
        else:
            print("❌ Invalid choice")
        
else:
    print("❌ Wrong PIN. Access denied.")


with open("notes.txt", "a") as f:
    note = input("write note: ")
    f.write( note + "\n")

with open("notes.txt", "r") as f:
    print(f.read())
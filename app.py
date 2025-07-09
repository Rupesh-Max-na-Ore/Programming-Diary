from database import add_entry, view_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit

Your selection: """

WELCOME = "Welcome to the programming diary!"

print(WELCOME)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Adding...")
        add_entry()
    elif user_input == "2":
        print("Viewing...")
        view_entries()
    else:
        print("Invalid option, please try again!")

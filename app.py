from database import add_entry, get_entries

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

        entry_content = input("What have you learned today? ")
        entry_date = input("Enter the date: ")

        add_entry(entry_content, entry_date)
    elif user_input == "2":
        print("Viewing...")

        entries = get_entries()
        for entry in entries:
            print(f"{entry['date']} \n {entry['content']} \n\n")
    else:
        print("Invalid option, please try again!")

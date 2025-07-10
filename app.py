from database import add_entry, create_table, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit

Your selection: """

WELCOME = "Welcome to the programming diary!"


def prompt_new_entry():
    """
    Prompts the user to enter what they have learned today and the date,
    then adds the entry to the database using the add_entry function.
    """
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)


def view_entries(entries):
    """
    Displays all diary entries passed as a list of tuples.
    Each entry is printed with its date and content.

    Args:
        entries (list of tuple): List of diary entries, where each entry is a tuple (content, date).
    """
    for entry in entries:
        print(f"{entry[1]} \n {entry[0]} \n\n")


print(WELCOME)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Adding...")
        prompt_new_entry()
    elif user_input == "2":
        print("Viewing...")
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")

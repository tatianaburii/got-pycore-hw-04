import re
from colorama import Fore, init

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if not validate_arguments(args, 2):
        return
    name, phone = args
    if not validate_phone(phone):
        return
    contacts[name] = phone
    print(Fore.GREEN + "Contact added.")

def validate_phone(phone):
    UA_SIMPLE = re.compile(r'^(?:\+?380|0)\d{9}$')
    if not phone.isdigit():
        return False
    if not UA_SIMPLE.match(phone):
        print(Fore.RED + "Error: Invalid phone number format. Please use Ukrainian format: +380XXXXXXXXX or 0XXXXXXXXX." + Style.RESET_ALL)
        return False
    return True

def validate_arguments(args, expected_count) -> bool:
    if len(args) != expected_count:
        print(Fore.RED + f"Error: Expected {expected_count} arguments, got {len(args)}.")
        return False
    return True

def get_contact_phone(args, contacts):
    name = args[0]
    if not validate_arguments(args, 1):
        return "Invalid arguments."
    print(Fore.YELLOW + contacts.get(name, "Contact not found."))

def print_all_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, phone in contacts.items():
        print(Fore.GREEN + f"{name}: " + Fore.YELLOW + f"{phone}")

def update_contact(args, contacts):
    name, phone = args
    validate_arguments(args, 2)
    if not validate_phone(phone):
        return
    if name in contacts:
        contacts[name] = phone
        print(Fore.GREEN + "Contact updated.")
    else:
        print("Contact not found.")

def main():
    init(autoreset=True)
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                return
            case "hello":
                print("How can I help you?")
            case "add":
                add_contact(args, contacts)
            case "change":
                update_contact(args, contacts)
            case "phone":
                get_contact_phone(args, contacts)
            case "all":
                print_all_contacts(contacts)
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
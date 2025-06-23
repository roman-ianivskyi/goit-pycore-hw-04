def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command, please use: add [ім'я] [номер телефону]"
    name, phone = args
    if contacts.get(name):
        return "Contact already exists, please use change username phone to update"
    else: 
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command, please use: change [ім'я] [новий номер телефону]"
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command, please use: phone [ім'я]"
    name = args
    phone = contacts.get(name)
    if phone:
        return phone
    else:
        return "Contact not found."

def show_all(args, contacts):
    if len(args) != 0:
        return "Invalid command, please use: all"
    if contacts:
        result = "Contact\t Phone\n"
        for contact, phone in contacts.items():
            result += f"{contact} \t {phone}\n"
        return result
    else:
        return "Contacts are empty"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

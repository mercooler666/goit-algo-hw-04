def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: Please provide both name and phone."
    name, phone = args[0], args[1]

    if not phone.isdigit(): # Я подумал, что логично добавить минимальную проверку ввода номера
        return "Error: Phone number must contain only digits."

    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: Please provide both name and phone."

    name, phone = args[0], args[1]

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."


def show_phone(args, contacts):
    if len(args) < 1:
        return "Error: Enter user name."

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."

    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if not command:
            continue

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
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
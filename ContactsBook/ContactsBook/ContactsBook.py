
MENU_PROMPT = "\nEnter 'a' to add a contact, 's' to see your contacts, 'f' to find a contact, or 'q' to quit: "
contacts = []


def add_contact():
    name = input("Please enter the name: ")
    number = input("Please enter the phone number: ")
    email = input("Please enter the email: ")

    contacts.append({
        'name': name,
        'number': number,
        'email': email
    })


def show_contacts():
    for contact in contacts:
        print_contact(contact)


def print_contact(contact):
    print(f"name : {contact['name']}"
          + f"number: {contact['number']}"
          + f"email: {contact['email']}"
          )


def find_contact():
    search_name = input(" What is the name that you are looking for: ")

    for contact in contacts:
        if contact["name"] == search_name:
            print_contact(contact)


user_options = {
    "a": add_contact(),
    "s": show_contacts(),
    "f": find_contact()
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Please chose between 'q', 'a', 's' and 'f' ")
            selection = input(MENU_PROMPT)


menu()
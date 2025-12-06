#contact base management system...............
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        if contact.name in self.contacts:
            print(f"Contact with name {contact.name} already exists.")
        else:
            self.contacts[contact.name] = contact
            print(f"Contact {contact.name} added.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} removed.")
        else:
            print(f"Contact with name {name} not found.")

    def update_contact(self, name, phone_number, email):
        if name in self.contacts:
            self.contacts[name].phone_number = phone_number
            self.contacts[name].email = email
            print(f"Contact {name} updated.")
        else:
            print(f"Contact with name {name} not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts.values():
            print(contact)

    def find_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print(f"Contact with name {name} not found.")


# Main Application
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Update Contact")
        print("4. List Contacts")
        print("5. Find Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)

        elif choice == '2':
            name = input("Enter name of contact to remove: ")
            contact_book.remove_contact(name)

        elif choice == '3':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contact_book.update_contact(name, phone_number, email)

        elif choice == '4':
            contact_book.list_contacts()

        elif choice == '5':
            name = input("Enter name of contact to find: ")
            contact_book.find_contact(name)
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again")
if __name__ == "__main__":
    main()

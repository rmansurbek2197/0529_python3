class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found")

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
        else:
            print("Contact not found")

    def display_contacts(self):
        for name, phone in self.contacts.items():
            print(f"Name: {name}, Phone: {phone}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name]}")
        else:
            print("Contact not found")


def main():
    contact_book = ContactBook()
    while True:
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Update contact")
        print("4. Display contacts")
        print("5. Search contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contact_book.add_contact(name, phone)
        elif choice == "2":
            name = input("Enter name: ")
            contact_book.delete_contact(name)
        elif choice == "3":
            name = input("Enter name: ")
            new_phone = input("Enter new phone: ")
            contact_book.update_contact(name, new_phone)
        elif choice == "4":
            contact_book.display_contacts()
        elif choice == "5":
            name = input("Enter name: ")
            contact_book.search_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
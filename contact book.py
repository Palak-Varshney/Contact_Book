class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found matching the search term.")

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nCONTACT MANAGER MENU")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number (press Enter to skip): ")
            new_email = input("Enter new email (press Enter to skip): ")
            new_address = input("Enter new address (press Enter to skip): ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
main()

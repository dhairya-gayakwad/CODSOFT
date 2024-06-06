class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone_number']}")
        else:
            print("Contact List is empty.")

    def search_contact(self, search_key):
        found_contacts = []
        for name, details in self.contacts.items():
            if search_key.lower() in name.lower() or search_key in details['phone_number']:
                found_contacts.append((name, details))
        return found_contacts

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            search_key = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_key)
            if found_contacts:
                print("Found Contacts:")
                for name, details in found_contacts:
                    print(f"Name: {name}, Phone: {details['phone_number']}")
            else:
                print("No contacts found.")
        
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            if name in contact_book.contacts:
                print("Enter new details (leave blank to keep existing)")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email address: ")
                address = input("Enter new address: ")
                contact_book.update_contact(name, phone_number, email, address)
            else:
                print(f"Contact '{name}' not found.")
        
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()


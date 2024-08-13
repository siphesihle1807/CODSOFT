import json
import os

# ASCII art for display purposes
art = """ ______   _    _   ______   ______   ______    ______   ______   ______   _    __ 
| |  | \ | |  | | / |  | \ | |  \ \ | |       | |  | \ / |  | \ / |  | \ | |  / / 
| |__|_/ | |--| | | |  | | | |  | | | |----   | |--| < | |  | | | |  | | | |-< <  
|_|      |_|  |_| \_|__|_/ |_|  |_| |_|____   |_|__|_/ \_|__|_/ \_|__|_/ |_|  \_\ 
                                                                                  """

# Class representing a single contact
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

# Class for managing a contact book
class ContactBook:
    def __init__(self, file_name):
        self.contacts = []  # List to store contacts
        self.file_name = file_name  # File name to load/save contacts
        self.load_contacts()  # Load contacts from file

    # Add a new contact
    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        self.save_contacts()  # Save contacts to file
        print("------------------------")
        print(f"Contact {name} added successfully!")
        print("------------------------")

    # Delete an existing contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save_contacts()  # Save contacts to file
                print("------------------------")
                print(f"Contact {name} deleted successfully!")
                print("------------------------")

                return
        print(f"Contact {name} not found. Please try adding it into the book.")

    # Update an existing contact
    def update_contact(self, name, new_name=None, new_phone_number=None, new_email=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_name:
                    contact.name = new_name
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                self.save_contacts()  # Save contacts to file
                print("------------------------")
                print(f"Contact {name} updated successfully!")
                print("------------------------")
                return
        print(f"Contact {name} not found. Please try adding it into the book.")

    # Search for a contact by name
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("------------------------")
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("------------------------")
                return
        print("------------------------")
        print(f"Contact {name} not found. Please try adding it into the book.")
        print("------------------------")

    # Display all contacts
    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the book!")
        else:
            for contact in self.contacts:
                print("------------------------")
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("------------------------")

    # Load contacts from file
    def load_contacts(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as file:
                    contacts_json = json.load(file)
                    for contact_json in contacts_json:
                        contact = Contact(contact_json['name'], contact_json['phone_number'], contact_json['email'])
                        self.contacts.append(contact)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading contacts: {e}")

    # Save contacts to file
    def save_contacts(self):
        contacts_json = []
        for contact in self.contacts:
            contacts_json.append({
                'name': contact.name,
                'phone_number': contact.phone_number,
                'email': contact.email
            })
        with open(self.file_name, 'w') as file:
            json.dump(contacts_json, file, indent=4)

# Main function to run the contact book application
def main():
    file_name = 'contacts.json'
    contact_book = ContactBook(file_name)

    while True:
        # Display menu
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            name = input("Enter name: ")
            contact_book.delete_contact(name)
        elif choice == "3":
            name = input("Enter name: ")
            new_name = input("Enter new name (press enter to skip): ")
            new_phone_number = input("Enter new phone number (press enter to skip): ")
            new_email = input("Enter new email (press enter to skip): ")
            contact_book.update_contact(name, new_name or None, new_phone_number or None, new_email or None)
        elif choice == "4":
            name = input("Enter name: ")
            contact_book.search_contact(name)
        elif choice == "5":
            contact_book.display_contacts()
        elif choice == "6":
            print("Okay, bye for now.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print(art)
    main()

import json

# File to store contact information
CONTACT_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def search_contact(contacts, query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return results

def update_contact(contacts, index, name, phone, email, address):
    if 0 <= index < len(contacts):
        contacts[index] = {'name': name, 'phone': phone, 'email': email, 'address': address}
        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts, index):
    if 0 <= index < len(contacts):
        removed_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact {removed_contact['name']} deleted successfully.")
    else:
        print("Contact not found.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = search_contact(contacts, query)
            if results:
                display_contacts(results)
            else:
                print("No contacts found.")
        elif choice == '4':
            display_contacts(contacts)
            index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            update_contact(contacts, index, name, phone, email, address)
        elif choice == '5':
            display_contacts(contacts)
            index = int(input("Enter the contact number to delete: ")) - 1
            delete_contact(contacts, index)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

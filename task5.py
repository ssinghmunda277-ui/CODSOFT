# Contact Management System

contacts = []

def add_contact():
    name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Enter Name or Phone Number to search: ")

    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found:")
            print(contact)
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter Store Name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("New Phone Number: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter Store Name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. please Try again.")
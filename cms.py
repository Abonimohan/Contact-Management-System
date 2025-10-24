# Contact Management System

# Dictionary to store contacts (name: phone)
contacts = {}

# Function to add a contact
def add_contact(name, phone):
    if name in contacts:
        print(f"\n{name} already exists. Updating the phone number.")
    contacts[name] = phone
    print(f"\nContact '{name}' added/updated successfully!")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"\nName: {name}\nPhone: {contacts[name]}")
    else:
        print(f"\nContact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    if not contacts:
        print("\nNo contacts available.")
    else:
        print("\n------ Contact List ------")
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")
        print("---------------------------")

# Main menu
def main():
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter name: ").title()
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to search: ").title()
            search_contact(name)
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            print("\nExiting Contact Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

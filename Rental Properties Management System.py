import json
import os

DATA_FILE = "properties.json"

# Load data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save data to JSON file
def save_data(properties):
    with open(DATA_FILE, "w") as f:
        json.dump(properties, f, indent=4)

# Generate a new property ID
def generate_id(properties):
    if not properties:
        return 1
    return max(p["property_id"] for p in properties) + 1

# Add a new property
def add_property(properties):
    owner = input("Enter owner's name: ")
    address = input("Enter property address: ")
    rent = float(input("Enter monthly rent: "))
    new_property = {
        "property_id": generate_id(properties),
        "owner_name": owner,
        "address": address,
        "rent_amount": rent,
        "is_rented": False,
        "tenant_name": ""
    }
    properties.append(new_property)
    print("Property added successfully!")

# View all properties
def view_properties(properties):
    if not properties:
        print("No properties found.")
        return
    for p in properties:
        status = "Rented" if p["is_rented"] else "Available"
        print(f"\nID: {p['property_id']}, Owner: {p['owner_name']}, Address: {p['address']}")
        print(f"Rent: ₹{p['rent_amount']}/month, Status: {status}, Tenant: {p['tenant_name']}")

# Search property by ID
def search_property(properties):
    pid = int(input("Enter property ID: "))
    for p in properties:
        if p["property_id"] == pid:
            print(f"\nOwner: {p['owner_name']}, Address: {p['address']}")
            print(f"Rent: ₹{p['rent_amount']}/month, Rented: {p['is_rented']}, Tenant: {p['tenant_name']}")
            return
    print("Property not found.")

# Update property details
def update_property(properties):
    pid = int(input("Enter property ID to update: "))
    for p in properties:
        if p["property_id"] == pid:
            print("Leave blank to keep current value.")
            owner = input(f"Owner [{p['owner_name']}]: ") or p['owner_name']
            address = input(f"Address [{p['address']}]: ") or p['address']
            rent_input = input(f"Rent [{p['rent_amount']}]: ")
            rent = float(rent_input) if rent_input else p['rent_amount']
            p.update({"owner_name": owner, "address": address, "rent_amount": rent})
            print("Property updated successfully!")
            return
    print("Property not found.")

# Delete a property
def delete_property(properties):
    pid = int(input("Enter property ID to delete: "))
    for i, p in enumerate(properties):
        if p["property_id"] == pid:
            properties.pop(i)
            print("Property deleted.")
            return
    print("Property not found.")

# Rent out a property
def rent_property(properties):
    pid = int(input("Enter property ID to rent: "))
    for p in properties:
        if p["property_id"] == pid:
            if p["is_rented"]:
                print("Property is already rented.")
                return
            tenant = input("Enter tenant's name: ")
            p["is_rented"] = True
            p["tenant_name"] = tenant
            print("Property rented successfully.")
            return
    print("Property not found.")

# Return a rented property
def return_property(properties):
    pid = int(input("Enter property ID to return: "))
    for p in properties:
        if p["property_id"] == pid:
            if not p["is_rented"]:
                print("This property is not rented.")
                return
            p["is_rented"] = False
            p["tenant_name"] = ""
            print("Property returned successfully.")
            return
    print("Property not found.")

# Main menu
def main():
    properties = load_data()
    while True:
        print("\n--- Rental Properties Management System ---")
        print("1. Add Property")
        print("2. View All Properties")
        print("3. Search Property by ID")
        print("4. Update Property")
        print("5. Delete Property")
        print("6. Rent a Property")
        print("7. Return a Property")
        print("8. Save and Exit")

        choice = input("Enter your choice (1–8): ")

        if choice == "1":
            add_property(properties)
        elif choice == "2":
            view_properties(properties)
        elif choice == "3":
            search_property(properties)
        elif choice == "4":
            update_property(properties)
        elif choice == "5":
            delete_property(properties)
        elif choice == "6":
            rent_property(properties)
        elif choice == "7":
            return_property(properties)
        elif choice == "8":
            save_data(properties)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

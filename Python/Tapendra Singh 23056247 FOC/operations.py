from read import load_inventory
from write import save_inventory, create_invoice
import datetime

# Function to display the current inventory
def display_inventory():
    # Load the current inventory from the data source
    inventory = load_inventory()
    
    # Check if the inventory is empty
    if not inventory:
        print("The inventory is currently empty.")
    else:
        # Print the table headers
        print("+----+-------------------------+-----------------+----------+--------+")
        print("| ID | Manufacturer            | Product Name    | Quantity | Price  |")
        print("+----+-------------------------+-----------------+----------+--------+")
        
        # Print each item's details
        for item in inventory:
            print(f"| {item['id']:2} | {item['manufacturer'][:23]:23} | {item['name'][:15]:15} | {item['quantity']:8} | ${item['price']:6.2f} |")
        
        # Print the table footer
        print("+----+-------------------------+-----------------+----------+--------+")

# Function to handle the purchase of furniture
def buy_furniture():
    # Load the current inventory from the data source
    inventory = load_inventory()
    
    # Prompt the user for their name
    emp_name = input("Enter your name: ")
    
    # Prompt the user for the item ID and quantity to purchase
    item_id = input("Enter the ID of the furniture to purchase: ")
    quantity = int(input("Enter the quantity to purchase: "))
    
    # Find the item in the inventory
    for item in inventory:
        if item['id'] == item_id:
            # Update the item's quantity in the inventory
            item['quantity'] += quantity
            print(f"{quantity} units of {item['name']} added to the inventory.")
            break
    else:
        # If the item is not found, print an error message
        print(f"Furniture with ID {item_id} not found.")
        return
    
    # Prepare the invoice data
    invoice_data = {
        "date": datetime.datetime.now(),
        "name": emp_name,
        "items": [
            {
                "id": item['id'],
                "manufacturer": item['manufacturer'],
                "name": item['name'],
                "quantity": quantity,
                "price": item['price']
            }
        ]
    }
    
    # Generate a filename for the invoice with a timestamp
    filename = f"purchase_invoice_{item_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Create the invoice and save the updated inventory
    create_invoice(invoice_data, filename)
    save_inventory(inventory)

# Function to handle the sale of furniture
def sell_furniture():
    # Load the current inventory from the data source
    inventory = load_inventory()
    
    # Prompt the user for the customer's name
    cust_name = input("Enter customer's name: ")
    
    # Initialize a list to track sold items and a variable for the total cost
    sales_list = []
    total_cost = 0
    
    # Loop to process sales transactions
    while True:
        # Prompt the user for the item ID and quantity to sell
        item_id = input("Enter the ID of the furniture to sell: ")
        quantity = int(input("Enter the quantity to sell: "))
        
        # Find the item in the inventory
        for item in inventory:
            if item['id'] == item_id:
                # Check if there is enough stock
                if item['quantity'] < quantity:
                    print(f"Not enough {item['name']} in stock. Only {item['quantity']} available.")
                    return
                
                # Update the item's quantity in the inventory
                item['quantity'] -= quantity
                
                # Add the item to the sales list and update the total cost
                sales_list.append({
                    "id": item['id'],
                    "manufacturer": item['manufacturer'],
                    "name": item['name'],
                    "quantity": quantity,
                    "price": item['price']
                })
                total_cost += item['price'] * quantity
                break
        else:
            # If the item is not found, print an error message
            print(f"Furniture with ID {item_id} not found.")
            return
        
        # Ask the user if they want to sell another item
        more_items = input("Sell another item? (y/n): ")
        if more_items.lower() != 'y':
            break
    
    # Prepare the invoice data
    invoice_data = {
        "date": datetime.datetime.now(),
        "name": cust_name,
        "items": sales_list
    }
    
    # Generate a filename for the invoice with a timestamp
    filename = f"sales_invoice_{cust_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Create the invoice and save the updated inventory
    create_invoice(invoice_data, filename)
    save_inventory(inventory)

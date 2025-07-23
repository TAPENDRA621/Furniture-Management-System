def load_inventory():
    # Initialize an empty list to hold inventory items
    inventory = []
    
    try:
        # Attempt to open the file 'inventory.txt' in read mode
        with open('inventory.txt', 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Strip leading/trailing whitespace and split the line by ', '
                parts = line.strip().split(', ')
                
                # Append a dictionary with item details to the inventory list
                inventory.append({
                    "id": parts[0],                        # Item ID
                    "manufacturer": parts[1],             # Manufacturer name
                    "name": parts[2],                     # Product name
                    "quantity": int(parts[3]),            # Quantity available (converted to int)
                    "price": float(parts[4].replace('$', ''))  # Price (converted to float, removing the '$' symbol)
                })
    except FileNotFoundError:
        # If the file does not exist, print a message and continue with an empty inventory
        print("Inventory file not found. Starting with an empty inventory.")
    
    # Return the inventory list
    return inventory

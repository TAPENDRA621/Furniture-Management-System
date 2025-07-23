VAT_RATE = 0.13  # VAT rate of 13%
SHIPPING_COST = 50  # Fixed shipping cost

# Function to save the inventory data to a file
def save_inventory(inventory):
    # Open 'inventory.txt' in write mode
    with open('inventory.txt', 'w') as file:
        # Iterate over each item in the inventory
        for item in inventory:
            # Write each item's details to the file in a formatted string
            file.write(f"{item['id']}, {item['manufacturer']}, {item['name']}, {item['quantity']}, ${item['price']}\n")

# Function to create an invoice and save it to a file
def create_invoice(invoice_data, filename):
    # Open the specified file in write mode
    with open(filename, 'w') as file:
        # Write the header of the invoice
        file.write("BRJ Furniture Stores - Invoice\n")
        file.write(f"Date: {invoice_data['date']}\n")
        file.write(f"Name: {invoice_data['name']}\n\n")
        
        # Write the table headers
        file.write("+----+-------------------------+-----------------+----------+--------+------------+\n")
        file.write("| ID | Manufacturer            | Product Name    | Quantity | Price  | Total      |\n")
        file.write("+----+-------------------------+-----------------+----------+--------+------------+\n")

        subtotal = 0  # Initialize subtotal for invoice items
        
        # Iterate over each item in the invoice
        for item in invoice_data['items']:
            # Calculate the total cost for the current item
            total = item['quantity'] * item['price']
            # Write the item details and total cost to the file
            file.write(f"| {item['id']:2} | {item['manufacturer'][:23]:23} | {item['name'][:15]:15} | {item['quantity']:8} | ${item['price']:6.2f} | ${total:10.2f} |\n")
            # Add the item total to the subtotal
            subtotal += total

        # Write the table footer
        file.write("+----+-------------------------+-----------------+----------+--------+------------+\n")
        
        # Calculate VAT and total amounts
        vat_amount = subtotal * VAT_RATE
        total_with_vat = subtotal + vat_amount
        total_amount = total_with_vat + SHIPPING_COST
        
        # Write the financial summary to the file
        file.write(f"\nSubtotal: ${subtotal:.2f}\n")
        file.write(f"VAT ({int(VAT_RATE * 100)}%): ${vat_amount:.2f}\n")
        file.write(f"Total with VAT: ${total_with_vat:.2f}\n")
        file.write(f"Shipping Cost: ${SHIPPING_COST:.2f}\n")
        file.write(f"Total Amount: ${total_amount:.2f}\n")
        file.write("\nThank you for your business!\n")

from operations import display_inventory, buy_furniture, sell_furniture

def main():
    while True:
        # Display the menu options
        print("\nWelcome to the Furniture Inventory System!")
        print("1. Show Inventory")
        print("2. Purchase Furniture")
        print("3. Sell Furniture")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1-4): ")

        # Handle the user's choice
        if choice == '1':
            display_inventory()
        elif choice == '2':
            buy_furniture()
        elif choice == '3':
            sell_furniture()
        elif choice == '4':
            print("Thank you for using the Furniture Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Entry point of the program
if __name__ == "__main__":
    main()

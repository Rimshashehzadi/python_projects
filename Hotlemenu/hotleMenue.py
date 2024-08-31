# # Define the menu of resturant

menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 80,
    'coffee': 100
}

# Greet
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs80\nCoffee: Rs100")

# Initialize order total
order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ").lower().strip()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1.title()}' has been added to your order")
else:
    print(f"Order item '{item_1.title()}' is not available!")

# Asking for another order
another_order = input("Do you want to order another item? (Yes/No): ").lower().strip()

# Check if the user wants to order more items
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower().strip()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2.title()}' has been added to your order")
    else:
        print(f"Order item '{item_2.title()}' is not available!")
else:
    print("No more items added.")

# Display the total amount
print(f"The total amount for the items is Rs{order_total}")

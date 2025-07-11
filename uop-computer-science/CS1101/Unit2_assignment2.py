############ Assignment Part 2
# Define a function that calculates the total cost of items based on item numbers.
# Each item has a fixed price, and discounts are applied based on the number of items purchased
# Global constant for item prices
PRICES = {1: 200.0, 2: 400.0, 3: 600.0}

def calculate_total_cost(item1=0, item2=0, item3=0):
    """Calculate total cost with discounts applied"""
    # Get list of items and calculate total using global prices
    items = [item for item in [item1, item2, item3] if item != 0]
    total_cost = sum(PRICES[item] for item in items)
    
    # Apply discounts based on number of items
    if len(items) == 2:
        total_cost *= 0.9  # 10% discount for two items
    elif len(items) >= 3:
        total_cost *= 0.75  # 25% discount for three or more items
    
    return items, total_cost

def print_order_summary(items, total_cost):
    """Print formatted order line for catalog display"""
    if len(items) == 1:
        # Single item
        item = items[0]
        product_name = f"Item {item}"
        print(f"{product_name:<40} {PRICES[item]}")
    else:
        # Multiple items - show as combo
        # e.g., [2,1,3] → sorted → ["Item 1", "Item 2", "Item 3"] → "Item 1 + Item 2 + Item 3"
        item_list = " + ".join([f"Item {item}" for item in sorted(items)])
        product_name = f"Combo ({item_list})"
        print(f"{product_name:<40} {total_cost:.1f}")

def display_catalog():
    """Display the complete online store catalog"""
    # Define all catalog combinations
    catalog_items = [
        (1,),           # Item 1
        (2,),           # Item 2
        (3,),           # Item 3
        (1, 2),         # Combo 1 (Item 1 + 2)
        (2, 3),         # Combo 2 (Item 2 + 3)
        (1, 3),         # Combo 3 (Item 1 + 3)
        (1, 2, 3)       # Combo 4 (Item 1 + 2 + 3)
    ]

    # Print catalog header
    print("Output:")
    print()
    print("Online Store")
    print("----------------------")
    print(f"{'Product(s)':<40} Price")

    # Print each catalog item
    for item_combo in catalog_items:
        # *item_combo unpacks tuple: (1,2,3) → calculate_total_cost(1, 2, 3)
        items, cost = calculate_total_cost(*item_combo)
        print_order_summary(items, cost)

    # Print catalog footer
    print("________________________")
    print()
    print("For delivery Contact:98764678899")

# Run the complete catalog display
display_catalog()

# Expected Output:
# Output:
#
# Online Store
# ----------------------
# Product(s)                               Price
# Item 1                                   200.0
# Item 2                                   400.0
# Item 3                                   600.0
# Combo (Item 1 + Item 2)                  540.0
# Combo (Item 2 + Item 3)                  900.0
# Combo (Item 1 + Item 3)                  720.0
# Combo (Item 1 + Item 2 + Item 3)         900.0
# ________________________
#
# For delivery Contact:98764678899
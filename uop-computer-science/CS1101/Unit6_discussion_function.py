# Part 1: The difference between object and value
"""
This code demonstrates the difference between object identity and equivalence in Python lists.
This situation is when a family goes to the grocery store and has a shared list.
"""
mom_list = ["egg", "milk", "bread", "fruit", "vegetables"]
dad_list = ["egg", "beef", "alcohol", "snack"]

def add_dad_items(grocery_list, dad_items=None):
    """Add dad's requested items to the grocery list if they're not already there."""
    if dad_items is None:
        return grocery_list
    
    for item in dad_items:
        if item not in grocery_list:
            grocery_list.append(item)
            print(f"Added dad's request '{item}' to the grocery list: {grocery_list}")
        else:
            print(f"'{item}' is already in the grocery list.")
    
    return grocery_list

def create_family_list(mom_list, dad_items=None):
    """Create a combined family grocery list starting with mom's list and adding dad's items."""
    # Create a copy of mom's list to avoid modifying the original
    family_list = mom_list[:]
    
    if dad_items:
        family_list = add_dad_items(family_list, dad_items)
    
    return family_list

# Create the combined shopping list
family_shopping_list = create_family_list(mom_list, dad_list)

print("\nMom's original shopping list:", mom_list)
print("Family shopping list:", family_shopping_list)
print("Are they the same object?", mom_list is family_shopping_list)  # False
print("Do they have the same values?", mom_list == family_shopping_list)  # False (dad added items)
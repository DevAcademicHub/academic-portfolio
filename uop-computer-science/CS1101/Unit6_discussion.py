# Part 1: The difference between object and value
"""
# This code demonstrates the difference between object identity and equivalence in Python lists.
# It shows how two lists can have the same contents but be different objects in memory.
# It also illustrates how to check if two lists are the same object or just have the same contents.
"""
mom_list = ["egg", "milk", "bread", "fruit", "vegetables"]
dad_list = ["egg", "milk", "bread", "fruit", "vegetables"]
shared_list = mom_list

# this shows the lists are not the same object in memory, but they are the same values.
print("Mom's list:", mom_list)
print("Dad's list:", dad_list)
print("Shared list:", shared_list)

# If mom_list and dad_list are the same object, they will have the same id.
# print("Mom's list ID:", id(mom_list))
# print("Dad's list ID:", id(dad_list))
# print("Shared list ID:", id(shared_list))

# equivalence check
print("Are mom_list and dad_list the same object?", mom_list is dad_list)
# This checks if both lists are the same object in memory, not if they have the same contents.
# Example: If mom_list and dad_list are created separately, this will return False even if they contain the same items.

# identity check
print("Are mom_list and shared_list the same object?", mom_list is shared_list)
# This checks if both lists are the same object in memory.
# Example: If shared_list is assigned to mom_list, this will return True because they reference the same object.

# Part 2: Objects, References, and Aliasing
mom_list = ["egg", "milk", "bread", "fruit", "vegetables"]
shared_list = mom_list

# Demonstrate aliasing effect
shared_list.append("cheese")
print("New mom's list: ", mom_list)

# Part 3: Combine all concepts
"""
This code demonstrates how to manipulate lists in Python, including adding and removing items.
It shows how to use methods like append, remove, and pop, and how these methods affect the list.
"""
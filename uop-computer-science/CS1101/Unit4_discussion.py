# Example 1: Precondition Violation (Argument Problem)
def calculate_average(numbers):
    """Calculate average of a list of numbers"""
    total = sum(numbers)
    return total / len(numbers)

# This will cause a precondition violation
try:
    result = calculate_average([])  # Empty list violates precondition
    print(f"Average: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Example 2: Postcondition Violation (Function Logic Problem)
def calculate_rectangle_area(length, width):
    """Calculate area of rectangle - but has a bug!"""
    area = length + width  # BUG: Should be length * width
    return area

# Function gets correct inputs but produces wrong result
length = 5
width = 3
result = calculate_rectangle_area(length, width)
print(f"Rectangle area: {result}") # Result should be 15, but will print 8
print(f"Expected: {length * width}") # Expected: 15

# Example 3: Return Value Usage Problem
def get_discount_rate(membership_type):
    """Returns discount rate as decimal (0.10 for 10%)"""
    if membership_type == "premium":
        return 0.15
    elif membership_type == "standard":
        return 0.10
    else:
        return 0.05

# Function works correctly but return value used wrong
price = 100
discount_rate = get_discount_rate("premium")
final_price = price - discount_rate  # BUG: Should be price * (1 - discount_rate)
print(f"Final price: ${final_price}") # Final price should be $85, but will print $85.0
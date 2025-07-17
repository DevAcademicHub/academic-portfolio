# 6.1 Return values
def compare_numbers(x, y):
    """Return -1 if x < y, 0 if x == y, and 1 if x > y."""
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

compare_numbers(5, 3)  # Returns 1

# 6.2 Incremental development
"""As an exercise, use incremental development to write a function called hypotenuse that
returns the length of the hypotenuse of a right triangle given the lengths of the other two
legs as arguments. Record each stage of the development process as you go."""
import math
def hypotenuse(a, b):
    """Return the length of the hypotenuse of a right triangle."""
    # Stage 1: Calculate the square of the legs
    a_squared = a ** 2
    b_squared = b ** 2
    
    # Stage 2: Sum the squares
    sum_of_squares = a_squared + b_squared
    # Stage 3: Calculate the square root of the sum
    return math.sqrt(sum_of_squares)
hypotenuse(3, 4)  # Returns 5.0


#6.4 Boolean functions
def is_between(x, y, z):
    """Return True if x <= y <= z, False otherwise."""
    return (x <= y <= z)

is_between(1, 2, 3)  # Returns True
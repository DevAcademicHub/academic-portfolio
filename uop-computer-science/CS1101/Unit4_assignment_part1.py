# Part1 Incremental development
"""Incremental Development Phases for Hypotenuse Function"""
import math
# Phase1: Initial Function Setup
def hypotenuse(a, b):
    return 0.0

# Test
result = hypotenuse(3, 4)  # Returns 0.0
print(f"Phase1: Initial Function Setup: {result}")  # Output: phase1: 0.0

# Phase2: Add Input Processing
def hypotenuse(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    print(f"a_squared: {a_squared}") # Output: a_squared: 9
    print(f"b_squared: {b_squared}") # Output: b_squared: 16
    return 0.0

# Test
result = hypotenuse(3, 4)  # Returns 0.0
print(f"Phase2: Add Input Processing: {result}")  # Output: phase2: 0.0

# Phase3: Add Sum of Squares Calculation
def hypotenuse(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    sum_of_squares = a_squared + b_squared
    print(f"sum_of_squares: {sum_of_squares}") # Output: sum_of_squares: 25
    return 0.0

# Test
result = hypotenuse(3, 4)  # Returns 0.0
print(f"Phase3: Add Sum of Squares Calculation: {result}")  # Output: phase3: 0.0

# Phase4: Add Square Root Calculation
def hypotenuse(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    sum_of_squares = a_squared + b_squared
    hypotenuse_length = math.sqrt(sum_of_squares)
    print(f"hypotenuse_length: {hypotenuse_length}") # Output: hypotenuse_length: 5.0
    return hypotenuse_length

# Test
result = hypotenuse(3, 4)  # Returns 5.0
print(f"Phase4: Add Square Root Calculation: {result}")  # Output: phase4: 5.0

# Phase5: Clean Final Version
def hypotenuse(a, b):
    """Return the length of the hypotenuse of a right triangle."""
    a_squared = a ** 2
    b_squared = b ** 2
    sum_of_squares = a_squared + b_squared
    return math.sqrt(sum_of_squares)

# Test
result = hypotenuse(3, 4)  # Returns 5.0
print(f"Phase5: Clean Final Version: {result}")  # Output: phase5: 5.0
print(f"Required Test 1: {hypotenuse(5, 12)}") # Output: Required Test 1: 13.0
print(f"Required Test 2: {hypotenuse(8, 6)}") # Output: Required Test 2: 10.0

# Final Version

# def hypotenuse(a, b):
#     """Return the length of the hypotenuse of a right triangle."""
#     # Stage 1: Calculate the square of the legs
#     a_squared = a ** 2
#     b_squared = b ** 2
    
#     # Stage 2: Sum the squares
#     sum_of_squares = a_squared + b_squared
#     # Stage 3: Calculate the square root of the sum
#     return math.sqrt(sum_of_squares)
# hypotenuse(3, 4)  # Returns 5.0
# Example 1 ################################################
# Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.
def multiply(number):  # "number" = parameter
    return number * 2

result = multiply(5)  # "5" = argument
print(result)                # output: 10

# Example 2 ################################################
# Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which. 

# Call 1: Using a VALUE as an argument
result1 = multiply(10)        # "10" is a literal value
print(result1)                # output: 20

# Call 2: Using a VARIABLE as an argument
my_num = 15
result2 = multiply(my_num)    # "my_num" is a variable
print(result2)                # output: 30

# Call 3: Using an EXPRESSION as an argument
result3 = multiply(5 + 3)     # "5 + 3" is an expression
print(result3)                # output: 16

# Example 3 ################################################
# Construct a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.
def local_variable_example():
    local_var = "local"  # This is a local variable
    return local_var

# Attempting to access the local variable outside the function
try:
    print(local_var)  # This will raise an error
except NameError as e:
    print(f"Error: {e}")    # output: Error: name 'local_var' is not defined
# The local variable "local_var" is not accessible outside the function


# Example 4 ################################################
"""
Construct a function that takes an argument.
Give the function parameter a unique name.
Show what happens when you try to use that parameter name outside the function.
Explain the results.
"""
def unique_parameter(param):  # "param" is a unique parameter name
    return param * 3
# Attempting to access the parameter name outside the function
try:
    print(param)  # This will raise an error
except NameError as e:
    print(f"Error: {e}")    # output: Error: name 'param' is not defined
# The parameter "param" is not accessible outside the function, leading to a NameError. 


# Example 5 ################################################
"""
Show what happens when a variable defined outside a function has the same name as a local variable inside a function. 
Explain what happens to the value of each variable as the program runs.
"""
temperature = 25  # Global variable
def check_temperature():
    temperature = 30  # Local variable with the same name
    print(f"Local temperature: {temperature}")  # Output: Local temperature: 30
    
    temperature = temperature + 5  # Reassigning the local variable
    print(f"Updated local temperature: {temperature}")  # Output: Updated local temperature: 35
    
check_temperature()
print(f"Global temperature: {temperature}")  # Output: Global temperature: 25


temperature = 25  # Global variable

def check_temperature():
    global temperature  # Declare we want to modify the global variable
    temperature = 30    # Now this modifies the global variable
    print(f"Local temperature: {temperature}")  # Output: 30
    
    temperature = temperature + 5  # Modifying the global variable
    print(f"Updated temperature: {temperature}")  # Output: 35
    
check_temperature()
print(f"Global temperature: {temperature}")  # Output: 35 (changed!)
    
# Example 6 ################################################
"""
PROBLEMATIC EXAMPLE: Global Variable Dependencies
This example demonstrates why global variables can cause serious issues in larger programs.
All functions below modify the same global account_balance, creating dependencies and
unpredictable behavior based on the order of function calls.
"""
account_balance = 1000  # Global variable

def withdraw_money(amount):
    global account_balance
    account_balance -= amount
    print(f"After withdrawal: ${account_balance}")

def apply_interest():
    global account_balance
    account_balance *= 1.02
    print(f"After interest: ${account_balance:.2f}")

def apply_fees():
    global account_balance
    account_balance -= 25
    print(f"After fees: ${account_balance:.2f}")

# Example showing order dependency problem:
print(f"Starting balance: ${account_balance}")  # Output: Starting balance: $1000

# Scenario 1: Fees first, then interest
withdraw_money(100)     # Output: After withdrawal: $900
apply_fees()           # Output: After fees: $875.00
apply_interest()       # Output: After interest: $892.50

print(f"Final balance (Scenario 1): ${account_balance:.2f}")  # Output: Final balance (Scenario 1): $892.50

# Reset for Scenario 2
account_balance = 1000
print(f"\nStarting balance: ${account_balance}")  # Output: Starting balance: $1000

# Scenario 2: Interest first, then fees
withdraw_money(100)     # Output: After withdrawal: $900
apply_interest()       # Output: After interest: $918.00
apply_fees()           # Output: After fees: $893.00

print(f"Final balance (Scenario 2): ${account_balance:.2f}")  # Output: Final balance (Scenario 2): $893.00


# Question2: Division by Zero Error Handling Tutorial

def get_user_input():
    """Get two numbers from user input"""
    num1 = float(input("Enter the first number (dividend): "))
    num2 = float(input("Enter the second number (divisor): "))
    return num1, num2

def perform_division_unsafe(num1, num2):
    """Perform division without zero check - will crash if num2 is 0"""
    result = num1 / num2
    print(f"Result of {num1} / {num2} = {result}")
    return result

def perform_division_safe(num1, num2):
    """Perform division with zero check"""
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        print("Division by zero is mathematically undefined.")
        print("Please enter a non-zero divisor.")
        return None

    result = num1 / num2
    print(f"Result of {num1} / {num2} = {result}")
    return result

def division_with_error():
    """Function that deliberately allows division by zero to demonstrate runtime errors"""
    print("\n=== PROBLEMATIC VERSION (Contains Runtime Error) ===")

    try:
        num1, num2 = get_user_input()
        perform_division_unsafe(num1, num2)

    except ZeroDivisionError as e:
        print(f"\nRUNTIME ERROR CAUGHT: {type(e).__name__}")
        print(f"Error Message: {e}")
        print("Cause: Division by zero is mathematically undefined!")
        print("The program attempted to divide by zero, which is not allowed.")

    except ValueError as e:
        print(f"\nINPUT ERROR: {type(e).__name__}")
        print(f"Error Message: {e}")
        print("Please enter valid numeric values only.")

def division_with_proper_handling():
    """Function demonstrating proper error handling for division operations"""
    print("\n=== FIXED VERSION (With Proper Error Handling) ===")

    try:
        num1, num2 = get_user_input()
        return perform_division_safe(num1, num2)

    except ValueError as e:
        print(f"Input Error: {e}")
        print("Please enter valid numeric values only.")
        return None

def main():
    """Main function to run the educational demonstration"""
    print("="*60)
    print("QUESTION 2: DIVISION BY ZERO ERROR HANDLING TUTORIAL")
    print("="*60)

    # Educational demonstration
    print("""
    To see the error in action, input 0 as the divisor when prompted

    DEMONSTRATION 1: Program with deliberate error
    """)
    division_with_error()

    print("\n" + "="*50)
    print("DEMONSTRATION 2: Program with proper error handling")
    division_with_proper_handling()

    print("""
    KEY TAKEAWAYS FOR JUNIOR DEVELOPERS:
    • Always validate user input before performing operations
    • Use try-except blocks to catch and handle runtime errors
    • Check for problematic values (like zero) before division
    • Provide clear, user-friendly error messages
    • Test your code with edge cases
    """)

if __name__ == "__main__":
    main()
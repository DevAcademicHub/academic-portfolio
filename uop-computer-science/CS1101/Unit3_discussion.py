def demonstrate_nested_conditionals(age):
    """Demonstrate nested conditionals with a simple example"""
    print("\n=== NESTED CONDITIONALS DEMONSTRATION ===")

    if age < 18:
        print("You are a minor.")
        if age < 13:
            print("You are a child.")
        else:
            print("You are a teenager.")
    else:
        print("You are an adult.")
        if age < 65:
            print("You are in your working years.")
        else:
            print("You are a senior citizen.")

def demonstrate_unnested_conditionals(age):
    """Demonstrate un-nested conditionals using elif chains"""
    print("\n=== UN-NESTED CONDITIONALS DEMONSTRATION ===")

    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    elif age < 65:
        print("You are an adult in your working years.")
    else:
        print("You are a senior citizen.")

def get_valid_age():
    """Get a valid age (positive integer) from user input"""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                return age
            else:
                print("Age must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    age = get_valid_age()
    demonstrate_nested_conditionals(age)
    demonstrate_unnested_conditionals(age)

if __name__ == "__main__":
    main()
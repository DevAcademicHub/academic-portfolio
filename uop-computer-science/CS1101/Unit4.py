def get_user_input():
    """Get a number from user input with validation"""
    try:
        num = int(input("Enter 1 number: "))
        return num
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_user_input()  # Recursive call for re-input

def process_number(num):
    """Process the number based on its value"""
    if num <= 0:
        return ""
    else:
        result = process_number(num - 1)
        return f"sexy\n{result}".rstrip()

def main():
    """Main function to run the program"""
    num = get_user_input()
    result = process_number(num)
    print(result)

if __name__ == "__main__":
    main()

# Example: Fixed Business Rules with Class Implementation
class NumberProcessor:
    def __init__(self):
        self.message = "sexy"  # Can be customized

    def get_user_input(self):
        """Get a number from user input with validation"""
        try:
            num = int(input("Enter 1 number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return self.get_user_input()  # Recursive call for re-input

    def process_number(self, num):
        """Process the number based on its value"""
        if num <= 0:
            return ""
        else:
            result = self.process_number(num - 1)
            return f"{self.message}\n{result}".rstrip()

    def run(self):
        """Main method to run the program"""
        num = self.get_user_input()
        result = self.process_number(num)
        if result:
            print(result)

# Usage
if __name__ == "__main__":
    processor = NumberProcessor()
    processor.run()

processor1 = NumberProcessor()
processor1.message = "Kiss you"

processor2 = NumberProcessor()
processor2.message = "Hello"

processor1.run()  # Prints "Kiss you" n times
processor2.run()  # Prints "Hello" n times
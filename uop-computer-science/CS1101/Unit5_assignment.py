
"""
Name String Operations Program
Demonstrates string manipulation and iteration concepts from Think Python Chapters 7-8
"""

def main():
    name = "Taichi"
    vowels = "aeiouAEIOU"

    while True:
        try:
            input_number = int(input(f"How many characters to display (1-{len(name)}): "))
            if input_number < 1 or input_number > len(name):
                print(f"Please enter a number between 1 and {len(name)}")
                continue

            print(f"Display {input_number} characters from left: {display_name(name, input_number)}")
            print(f"The number of vowels: {count_vowels(name, vowels)}")
            print(f"The reversed name: {reverse_name(name)}")
            break

        except ValueError:
            print("Please enter a valid number")
            continue

# Extract first n characters from the name using string slicing
def display_name(name, n):
    return name[:n]

# Count the number of vowels in the name
def count_vowels(name, vowels):
    count = 0
    for c in name:
        if c in vowels:
            count += 1
    return count

# Reverse the name using Python's string slicing with negative step.
def reverse_name(name):
    return name[::-1]

# test cases
def run_tests():
    assert display_name("Taichi", 3) == "Tai"
    assert count_vowels("Taichi", "aeiouAEIOU") == 3
    assert reverse_name("Taichi") == "ihciaT"
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
    print("\n--- Main Program ---")
    main()
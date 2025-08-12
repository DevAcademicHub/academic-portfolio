# Example: Handling FileNotFoundError with try-except blocks
def read_file_safely(filename):
    """
    Demonstrates exception handling for file operations
    as described in Think Python Chapter 14
    """
    try:
        # Try to open and read the file
        fin = open(filename, 'r')
        content = fin.read()
        fin.close()
        print(f"File content:\n{content}")
        return content
    except FileNotFoundError as e:
        print(f"Error: The file '{filename}' does not exist.")
        print("Technical details:", e)
        return None
    # except IOError:
    #     # Handle other I/O related errors
    #     print(f"Error: Unable to read the file '{filename}'.")
    #     print("There was an I/O error accessing the file.")
    #     return None


result = read_file_safely("nonexistent.txt")

result = read_file_safely("Unit8_discussion_test.txt")
print("Result of reading Unit8_discussion_test.txt: ", result)

with open("Unit8_discussion_test.txt", "a") as f:
    f.write("\nThis is a test file.")

result = read_file_safely("Unit8_discussion_test.txt")
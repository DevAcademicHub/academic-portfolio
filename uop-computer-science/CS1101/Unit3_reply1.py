def get_valid_score():
    """
    Get a valid score (0-100) from user input.
    Handles invalid inputs and ensures score is within range.
    """
    while True:
        try:
            score = int(input("Enter your score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_result(score):
    """
    Check if the score is passing or failing.
    Simple one-level conditional.
    """
    if score >= 50:
        print("You passed.")
    else:
        print("You failed.")

# Main program
def main():
    # Get validated score
    score = get_valid_score()

    # Check result
    check_result(score)

if __name__ == "__main__":
    main()



def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)
    else:
        print('Blastoff!')

# For loop version of countdown  
def countdown(n):
    for i in range(n, 0, -1):
        print(i)
    print('Blastoff!')


print (1,000,000) # Output: 1000000
percentage = ( 60 * 100) // 55
print (percentage) # Output: 109 (integer division)
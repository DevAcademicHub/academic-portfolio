# Question1
def countdown(n):
    """Count down from n to 0, returning each number, and end with 'Blastoff!'"""
    if n <= 0:
        return 'Blastoff!'
    else:
        return f"{n}\n{countdown(n-1)}"

def countup(n):
    """Count up from n to 0, returning each number, and end with 'Blastoff!'"""
    if n >= 0:
        return 'Blastoff!'
    else:
        return f"{n}\n{countup(n+1)}"

def count(n):
    """Return countdown or countup based on n value"""
    if n < 0:
        return countup(n)
    else:
        return countdown(n)

def main():
    """Main function to demonstrate the count functions"""
    n = int(input("Enter a number: "))
    print(count(n))

if __name__ == "__main__":
    main()
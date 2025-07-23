# Unit 4 Assignment Part 2: Password Check Function
# Incremental development approach

import string

# Phase 1: Initial setup
# Goal: Create function skeleton that always returns False
# This establishes the function signature before adding logic
def check_password(password):
    return False

print(f"Phase 1: {check_password('MyP@ssw0rd')}")

# Phase 2: Length check
# Goal: Add minimum length requirement (8 characters)
# Length is the first line of defense against brute force attacks
def check_password(password):
    if len(password) < 8:
        return False
    return False  # Still building incrementally

print(f"Phase 2: {check_password('short')} {check_password('MyP@ssw0rd')}")

# Phase 3: Add all requirements
# Goal: Implement complete password validation
# Checks for uppercase, lowercase, digits, and special characters
# This ensures passwords have character variety to resist attacks
def check_password(password):
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    return has_upper and has_lower and has_digit and has_special

print("Phase 3:")
for pwd in ["weak", "Weak123", "MyP@ssw0rd"]:
    print(f"  {pwd}: {check_password(pwd)}")

# Phase 4: Final version
# Goal: Refactor for clarity using early returns
# Each check explicitly shows what's missing if password fails
# This "fail fast" approach is a common pattern in validation code
def check_password(password):
    """Check if password meets all security requirements."""
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True

# Test final version
print("\nFinal tests:")
tests = [
    ("password", False),
    ("Password1", False),
    ("P@ssw0rd", True),
    ("MySecureP@ss1", True)
]

for pwd, expected in tests:
    result = check_password(pwd)
    print(f"  {pwd}: {result} {'✓' if result == expected else '✗'}")

# Phase 5: improve readability
# Goal: Use descriptive variable names and comments
# This enhances maintainability and makes the code self-documenting
def check_password(password):
    """Check if password meets all security requirements."""
    if len(password) < 8:
        return False  # Password too short
    has_upper = any(c.isupper() for c in password)  # Check for uppercase letters
    has_lower = any(c.islower() for c in password)  # Check for lowercase letters
    has_digit = any(c.isdigit() for c in password)  # Check for digits
    has_special = any(c in string.punctuation for c in password)  # Check for special characters
    
    return has_upper and has_lower and has_digit and has_special
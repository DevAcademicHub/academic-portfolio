# Example 6 ################################################
"""
SOLUTION: Fixed Business Rules - Eliminates Order Dependency
This example demonstrates how to solve both global variable problems AND order dependency.
"""

# Approach 1: Parameter Passing with Fixed Business Rules
def process_account_transaction(initial_balance, withdrawal_amount):
    """
    Process account transaction with fixed business rules:
    1. Withdraw money first
    2. Apply fees second  
    3. Apply interest last
    """
    balance = initial_balance - withdrawal_amount  # Withdraw
    balance = balance - 25                        # Apply fees
    balance = balance * 1.02                      # Apply interest
    return balance

# Usage - always same result regardless of how you call it
balance1 = process_account_transaction(1000, 100)
print(f"Final balance (approach 1): ${balance1:.2f}")  # Always: $892.50

# Approach 2: Class with Fixed Business Rules
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def process_transaction(self, withdrawal_amount):
        """
        Process transaction with fixed business rules:
        1. Withdraw money first
        2. Apply fees second
        3. Apply interest last
        """
        self.balance -= withdrawal_amount  # Withdraw
        self.balance -= 25                # Apply fees
        self.balance *= 1.02              # Apply interest

# Usage with class - always same result
account = BankAccount(1000)
account.process_transaction(100)
print(f"Final balance (approach 2): ${account.balance:.2f}")  # Always: $892.50

# Demonstration: No matter how you call it, result is consistent
account2 = BankAccount(1000)
account2.process_transaction(100)
print(f"Consistent result: ${account2.balance:.2f}")  # Always: $892.50
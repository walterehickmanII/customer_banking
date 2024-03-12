"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
import pandas as pd
from pathlib import Path
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    class SavingsAccount:
        def __init__(self, balance, interest_rate):
            self.balance = balance(0.00)
            self.interest_rate = interest_rate(0.00)

        def calculate_interest(self, months):
        # Convert annual interest rate to monthly interest rate
            monthly_interest_rate = self.interest_rate / 12
        
        # Calculate interest earned
            interest_earned = self.balance * monthly_interest_rate * months
        
        # Update account balance
            updated_balance = self.balance + interest_earned
        
            return updated_balance, interest_earned

        def set_balance(self, updated_balance):
            self.balance = updated_balance

    def set_interest(self, interest_earned):
        self.interest_rate = interest_earned


# Example usage:
if __name__ == "__main__":
    initial_balance = 1000
    annual_interest_rate = 0.05  # 5% annual interest rate
    num_months = 6
    
    account = create_savings_account(initial_balance, annual_interest_rate, months = 12)
    
    updated_balance, earned_interest = account.calculate_interest(num_months)
def calculate_interest(balance, interest_rate, months):
    monthly_interest_rate = interest_rate / 12
    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = balance * monthly_interest_rate * months
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_interest(earned_interest)
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return updated_balance, interest_earned
"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import account 

                            
def create_cd_account(balance(float), interest_rate(float), months(int)):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
class cd_account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
       

    def deposit(self, amount):
        self.balance += amount 


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")


    # Calculate interest earned
    # ADD YOUR CODE HERE
    def calculate_interest(balance, interest, months):
     interest = balance * interest * months 

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    def calc_account_balance(balance += interest):
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
        def set_balance(self, updated_balance):
            self.balance = updated_balance
        print("New balance:", account.balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    def set_interest(self, interest):
            self.interest_rate = interest
    # Return the updated balance and interest earned.
     # ADD YOUR CODE HERE
    def calculate_Interest(self):
        return self.balance * self.interest
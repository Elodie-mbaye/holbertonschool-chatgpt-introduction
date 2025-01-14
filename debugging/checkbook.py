#!/usr/bin/python3
class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance inquiries.

    Attributes:
    - balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """
        Initialize a Checkbook instance with a balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
        - amount (float): The amount to deposit. Must be a positive number.

        Returns:
        None
        """
        if amount < 0:
            print("Invalid deposit amount. Please enter a positive number.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Parameters:
        - amount (float): The amount to withdraw. Must be a positive number and not exceed the current balance.

        Returns:
        None
        """
        if amount < 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance in the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    The main function for interacting with the Checkbook.
    Provides a menu to deposit, withdraw, check balance, or exit the program.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Thank you for using the Checkbook! Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()


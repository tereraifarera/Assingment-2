class BankAccount:
    """A bank account that protects its balance using encapsulation."""

    def __init__(self, owner, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner                  # public attribute
        self.__account_number = id(self)    # private attribute (name-mangled)
        self.__balance = initial_balance    # private attribute (name-mangled)

    # Public interface: the only sanctioned way to change the balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited ${amount:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        print(f"Withdrew ${amount:,.2f}")

    def get_balance(self):
        """Read-only access to the balance."""
        return self.__balance

    def display_balance(self):
        print(f"{self.owner}'s balance: ${self.__balance:,.2f}")


def main():
    account = BankAccount("Alice", 1000)
    account.display_balance()

    # 1. Using the public methods (validated, safe)
    account.deposit(500)
    account.withdraw(200)
    account.display_balance()

    # 2. Validation protects the balance
    print("\n--- Validation in action ---")
    for action, amount in [(account.withdraw, 5000), (account.deposit, -50)]:
        try:
            action(amount)
        except ValueError as e:
            print(f"Error: {e}")

    # 3. Direct access to the private attribute fails
    print("\nrying to bypass the methods")
    try:
        print(account.__balance)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    account.__balance = 1_000_000
    account.display_balance()

    print("\n --- Name mangling---")
    print("Attributes:", [a for a in vars(account)])
    print("Balance:", account.get_balance())

if __name__ == "__main__":
    main()
class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = account_id
        self.balance = balance
        self.transactions = []

    def get_balance(self):
        return self.balance

    def add_funds_via_transfer(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.transactions.append(f"Incoming transfer: {amount}")
        return self.balance

    def schedule_payment(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(f"Scheduled payment: {amount}")
        return self.balance

    def transfer(self, target_account, amount):
        self.schedule_payment(amount)
        target_account.add_funds_via_transfer(amount)
        self.transactions.append(f"Transfer to {target_account.account_id}: {amount}")
        return self.balance

    def get_transaction_history(self):
        return self.transactions


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, username, password):
        self.logged_in = self.username == username and self.password == password
        return self.logged_in

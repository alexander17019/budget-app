class Category:


    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        return "This is a category string"

    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})

    def withdrawal(self, amount, description):
        if self.check_balance():
            self.ledger.append({"amount": -amount, "description": description})
            return True;
        return False

    def check_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]

        return total_cash

    def transfer(self, amount, category):
        if self.check_balance(amount):
            self.withdrawal(amount, "transfer to " + category.name)
            category.deposit(amount, "transfer to " + self.name)
            return True
        return False

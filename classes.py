class Category:

    def __init__(self, category, budget):
        self.category = category
        self.budget = budget

    def deposit(self, budget):
        self.budget = budget
        return "this amount has been deposited {} in category".format(self.budget, self.category)

    def check_balance(self):
        return "This is the current balance: {}".format(self.budget)

    def withdrawal(self):
        return "You have withdrawn this amount"

    def transfer(self):
        pass

    def print_balance(self):
        pass


clothing_category = ("clothing", 1000)
food_category = ("Food", 1000)
entertainment_category = ("Entertainment", 1000)
car_category = ("Car expenses", 1000)
miscelleous_category = ("Miscelleous", 1000)
house_category = ("House rent", 1000)

print(food_category.deposit())

import budget
from budget import Category

food: Category = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdrawal(200, "groceries")
food.withdrawal(300, "takeouts")
print("Total_food_balance")
print(food.check_balance())
clothing = budget.Category("Clothing")
clothing.deposit(2000, "initial deposit")
clothing.withdrawal(300, "jeans")
clothing.withdrawal(400, "shirts")
print("Total_clothing_balance")
print(clothing.check_balance())

print(food)
print(clothing)


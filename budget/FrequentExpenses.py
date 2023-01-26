import matplotlib.pyplot as plt
from . import Expense
import collections
expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")
spending_categories = list()
for expense in expenses.list:
    spending_categories.append(expense.category)
spending_counter = collections.Counter(spending_categories)
print(spending_counter)
top5 = spending_counter.most_common(5)
print(top5)
categories, count = zip(*top5)
print(categories)
print(count)
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
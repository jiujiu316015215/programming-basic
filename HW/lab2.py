import math
SALES_TAX = .0735
num_items = 2
cost_per_item = 7.59
price = cost_per_item * (1 + SALES_TAX) * num_items
print ("The price is $%.2f" % price)

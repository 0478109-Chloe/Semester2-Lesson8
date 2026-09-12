# In class, we made a 

import random

def count_occurrence(item, my_list):
    total = 0
    for i in my_list:
        if i == item:
            total += 1 # total = total + 1
    return total

# mom bought a lot of grocery items
grocery_item = ["apple", "banana", "broccoli", "milk", "bread"]
shopping_cart = []

for i in range(100):
    # throws random items from grocery_item into shopping_cart
    shopping_cart.append(random.choice(grocery_item))

print(shopping_cart)

print("Mom bought:")
print(str(count_occurrence("apple", shopping_cart)) + " apples")
print(str(count_occurrence("banana", shopping_cart)) + " bananas")
print(str(count_occurrence("broccoli", shopping_cart)) + " broccolis")
print(str(count_occurrence("milk", shopping_cart)) + " gallons of milk")
print(str(count_occurrence("bread", shopping_cart)) + " loaves of bread")







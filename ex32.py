hairs = ["brown", "blond", "red"]
eyes = ["brown", "blue", "green"]
weights = [1, 2, 3, 4]

count = [1, 2, 3, 4, 5]
fruitTypes = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in count:
    print(f"This is count {number}.")

for fruit in fruitTypes:
    print(f"A fruit of type: {fruit}.")

for i in change:
    print(f"I got {i}.")

# Create a new empty list
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list...")
    elements.append(i)

# Print all elements
for el in elements:
    print(f"Element was {el}.")

def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxesOfCrackers} boxes of Crackers!")
    print("Man that's enough for a party.")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheeseAndCrackers(20, 30)

print("OR, we can use variables from our script:")
amountOfCheese = 10
amountOfBoxes = 50

cheeseAndCrackers(amountOfCheese, amountOfBoxes)

print("We can even do math inside too:")
cheeseAndCrackers(10 + 5, 10 + 2)

print("And we can combine the two, variables and math:")
cheeseAndCrackers(amountOfCheese + 10, amountOfBoxes + 20)

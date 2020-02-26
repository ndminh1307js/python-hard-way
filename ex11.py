print("How old are you?", end=' ')
age = int(input())
print("How tall are you?", end=' ')
height = int(input())
print("How much do you weigh?", end=' ')
weight = int(input())

print(
    f"So, you're {age} years old, {height} centimeters tall and {weight} heavy")

print(type(age), type(height), type(weight))

print('Total of your age, height and weight is', age + height + weight)

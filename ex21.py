def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


def substract(a, b):
    print(f"Substracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b


print("Let's do some math with just functions.")

age = add(20, 4)
height = substract(78, 4)
weight = multiply(2, 90)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway

print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes {what}. Can you do it by hand?")


def addByInput():
    a = float(input("Enter a's value: "))
    b = float(input("Enter b's value: "))
    sum = a + b
    return f"Adding {a} + {b} = {sum}"


print(addByInput())

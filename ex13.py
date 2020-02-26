from sys import argv
# read the WYSS section for how to run this
print(argv)
script, first, second, third = argv  # list of arguments as strings

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(type(first))

fourth = input("Your fourth variable is: ")
fifth = input("Your fifth variable is: ")

print(fourth, fifth)

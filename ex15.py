from sys import argv

script, filename = argv

txtFile = open(filename)
print(txtFile.name)

print(f"Here is your file: {filename}")
print(txtFile.read())

print("Type the filename again:")
fileAgain = input('> ')

txtAgain = open(fileAgain)

print(txtAgain.read())

from sys import argv

script, filename = argv

print("Opening the file...")
target = open(filename, 'r')

print("The file content is shown below: ")
contents = target.read()
print(contents)

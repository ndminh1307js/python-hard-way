# Review
from sys import argv

script, filename = argv

target = open(filename, 'r+')

# Load note


def loadNote():
    notes = target.read()
    return notes

# Add note


def addNote(newNote):
    notes = loadNote()
    notes = notes + "\n" + newNote
    print(notes)
    open(filename, 'w').close()
    target.write(notes)
    return newNote


addNote("I have died every day waiting for you")

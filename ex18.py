# this one is like your scripts with argv
def printTwo(*argv):
    arg1, arg2 = argv
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *argv is actually pointless, we can just do this


def printTwoAgain(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument


def printOne(arg):
    print(f"arg: {arg}")

# this one takes no arguments


def printNone():
    print(f"I got nothing.")


printTwo('Christopher', 'Nolan')
printTwoAgain('Cristian', 'Bale')
printOne('Heath Ledger')
printNone()

# Checklist


def checkList(exercise):
    checklistFile = open('files/checklist.txt', 'a')
    checklistFile.write(exercise)
    checklistFile.write('\n')
    checklistFile.close()


checkList('exercise 1')
checkList('exercise 2')
checkList('exercise 3')

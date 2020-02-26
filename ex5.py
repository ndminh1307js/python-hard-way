myName = 'Damian Ngo'
myAge = 23  # not a lie
myHeight = 180  # centimeters
myHeightInInches = round(myHeight / 2.54)  # convert my height to inches
myWeight = 98  # kilos
myWeightInPounds = round(myWeight / 2.20462262)  # convert my weight to pounds
myEyes = 'Black'
myTeeth = 'White'
myHair = 'Black'

print(f"Let's talk about {myName}.")
print(f"He's {myHeight} tall.")
print(f"He's {myWeight} heavy.")
print("Actually that's too heavy.")
print(f"He's got {myEyes} eyes and {myHair} hair.")
print(f"His teeth are usually {myTeeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = myAge + myHeight + myWeight
print(f"If I add {myAge}, {myHeight} and {myWeight} I get {total}")

# Print results converted
print(f"He's {myHeightInInches} inches tall.")
print(f"He's {myWeightInPounds} pounds heavy.")

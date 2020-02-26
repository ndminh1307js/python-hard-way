from sys import argv

script, userName = argv
prompt = 'Type your answer and press Enter: '

print(f"Hi {userName}, I'm {script} script.")
print("I would like to ask you a few questions.")
print(f"Do you like me, {userName}?")
likes = input(prompt)

print(f"Where do you live, {userName}")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
  Alright, so you said {likes} about liking me.
  You live in {lives}. Not sure where that is.
  And you a {computer} computer. Nice. Welcome.
""")

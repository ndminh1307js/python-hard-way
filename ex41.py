import random
from urllib.request import urlopen
import sys

wordUrl = "http://learncodethehardway.org/words.txt"

words = []

phrases = {
    "class %%%(%%%):": "Make a class named %%% that is - a %%%",
    "class %%%(object):\n\tdef __init__(self, ***):": "class %%% has a __init__ that takes self and *** as params",
    "class %%%(object):\n\tdef ***(self, @@@):": "class %%% has a function *** that take self and @@@ as params",
    "***= %%%()": "Set *** to an instance of class %%%",
    "***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'"
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    phraseFirst = True
else:
    phraseFirst = False

# load up the words from website
for word in urlopen(wordUrl).readlines():
    words.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    classNames = [w.capitalize()
                  for w in random.sample(words, snippet.count("%%%"))]
    otherNames = random.sample(words, snippet.count("***"))
    results = []
    paramNames = []

    for i in range(0, snippet.count("@@@")):
        paramCount = random.randint(1, 3)
        paramNames.append(', '.join(random.sample(words, paramCount)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in classNames:
            result = result.replace('%%%', word, 1)

        # fake other names
        for word in otherNames:
            result = result.replace('***', word, 1)

        # fake parameter lists
        for word in paramNames:
            result = result.replace('@@@', word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(phrases.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)

            if phraseFirst:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")

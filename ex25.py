from ex25_lib import breakWords, sortWords, printFirstWord, printLastWord, sortSentence, printFirstAndLast, printFirstAndLastSorted
sentence = "All good things come to those who wait"

words = breakWords(sentence)
sortedWords = sortWords(words)
printFirstWord(words)
printLastWord(words)
printFirstWord(sortedWords)
printLastWord(sortedWords)

sortedWords = sortSentence(sentence)
printFirstAndLast(sentence)
printFirstAndLastSorted(sentence)

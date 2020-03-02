import sys

script, inputEncoding, error = sys.argv


def main(languageFile, encoding, errors):
    line = languageFile.readline()
    if line:
        printLine(line, encoding, errors)
        return main(languageFile, encoding, errors)


def printLine(line, encoding, errors):
    nextLang = line.strip()
    rawBytes = nextLang.encode(encoding, errors=errors)
    cookedStr = rawBytes.decode(encoding, errors=errors)

    print(rawBytes, "<=====>", cookedStr)


languages = open("languages.txt", encoding="utf-8")

main(languages, inputEncoding, error)

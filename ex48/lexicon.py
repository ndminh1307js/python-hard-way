WORD_TYPES = {
    'north': 'direction',
    'south': 'direction',
    'west': 'direction',
    'east': 'direction',
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun'
}


def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None


# print(WORD_TYPES.get('sdsd')) = None

def scan(sentence):
    words = sentence.split(' ')
    results = []

    for word in words:
        word_type = WORD_TYPES.get(word)

        if word_type == None:
            number = convert_number(word)

            if number != None:
                results.append(('number', number))
            else:
                results.append(('error', word))
        else:
            results.append((word_type, word))

    return results


print(scan("The princess who you've just saved from the bear in the cabinet"))

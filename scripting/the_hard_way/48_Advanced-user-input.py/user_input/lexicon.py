def scan(sentence):

    words = sentence.split()

    # tuples with words
    nouns       = ('door', 'bear', 'princess', 'cabonet')
    directions  = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
    verbs       = ('go', 'stop', 'kill', 'eat')
    stop_words  = ('the', 'in', 'of', 'from', 'at', 'it')
    # numbers   -- about the numbers... maybe use int() in some way and if it raises an error get None (try/except)
    
    result = [] # list to be returned

    for word in words:
        if word in nouns:
            result.append(('noun', word))
        elif word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stop_words:
            result.append(('stop', word))
        else:
            try:
                num = int(word)
                result.append(('number', num))
            except ValueError:
                result.append(('error', word))

    return result

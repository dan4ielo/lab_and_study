class ParserError(Exception):
    pass

class Sentence():

    def __init__(self, subject, verb, object):
        # We take in ('noun', 'princess') tuples and convert them
        self.subject    = subject[1]
        self.verb       = verb[1]
        self.object     = object[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list

        if word[0] == expecting:
            return word[1]
        else:
            return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
    return

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek (word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    elif next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list, subj):
    verb = parse_verb(word_list)        # Literally, 0 idea what he was trying to do
    obj = parse_object(word_list)       # and how to fix it. How is this supposed to work?

    return Sentence(subj, verb, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # Assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else: 
        raise ParserError('Must start with subject, object or verb not: {}'.format(start))

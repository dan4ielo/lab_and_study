from nose.tools import *
from user_input import parser_ex49

list_of_words = [
    ('noun', 'princess'),
    ('noun', 'door'),
    ('verb', 'go'),
    ('verb', 'kill'),
    ('direction', 'north')
]

def test_peek():

    for word in list_of_words:
        assert_equal(parser_ex49.peek(word), word[0])

def test_match():
    
    assert_equal(parser_ex49.match(list_of_words[0], 'noun'), 'princess')
    assert_equal(parser_ex49.match(list_of_words[1], 'noun'), 'door')

def test_parse_verb():

    for word in list_of_words:
        if word[0] == 'verb':
            assert_equal(parser_ex49.parse_verb(word), word[1])
        else:
            assert_raises(parser_ex49.ParserError, parser_ex49.parse_verb, word)

def test_parse_object():
    
    for word in list_of_words:
        if word[0]=='noun' or word[0]=='direction':
            assert_equal(parser_ex49.parse_object(word), word[1])
        else:
            assert_raises(parser_ex49.ParserError, parser_ex49.parse_object, word)

#def parse_subject(word_list, subj):
#    verb = parse_verb(word_list)
#    obj = parse_object(word_list)
#
#    return Sentence(subj, verb, obj)

#def parse_sentence(word_list):
#    skip(word_list, 'stop')

#    start = peek(word_list)

#    if start == 'noun':
#        subj = match(word_list, 'noun')
#        return parse_subject(word_list, subj)
#    elif start == 'verb':
#        # Assume the subject is the player then
#        return parse_subject(word_list, ('noun', 'player'))
#    else: 
#        raise ParseError('Must start with subject, object or verb not: {}'.format(start))

def test_parse_sentence():
   
    for word in list_of_words:
        if word[0] == 'noun':
            assert_equal(parser_ex49.parse_sentence(word), parser_ex49.parse_subject(word,word[1]))
        elif word[0]=='verb':
            assert_equal(parser_ex49.parse_sentence(word), parser_ex49.parse_subject(word, ('noun', 'player')))
        else:
            assert_raises(parser_ex49.ParserError, parser_ex49.parse_sentence, word)

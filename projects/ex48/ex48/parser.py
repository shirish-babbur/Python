class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, typ):
    if word_list:
        word = word_list.pop(0)

        if word[0] == typ:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, typ):
    while peek(word_list) == typ:
        match(word_list, typ)

def parse_verb(word_list):
    skip(word_list, 'stop_word')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next")

def parse_object(word_list):
    skip(word_list, 'stop_word')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next")

def parse_subject(word_list):
    skip(word_list, 'stop_word')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a noun or verb next")

def parse_sentence(word_list):
    subject = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subject, verb, obj)

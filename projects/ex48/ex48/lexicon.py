from ex48.ex48_convert import convert_numbers

verbs = [('verb','go'), ('verb', 'stop'), ('verb', 'kill'), ('verb', 'eat')]
directions = [('direction', 'north'), ('direction', 'south'), ('direction', 'east'), ('direction', 'west'), ('direction', 'up'), ('direction', 'down'),
                ('direction', 'left'), ('direction', 'right'), ('direction', 'back')]
stop_words = [('stop_word', 'the'), ('stop_word', 'in'), ('stop_word', 'of'), ('stop_word', 'from'), ('stop_word', 'at'), ('stop_word', 'it')]
nouns = [('noun', 'door'), ('noun', 'bear'), ('noun', 'princess'), ('noun', 'cabinet')]
numbers = [('number', 0), ('number', 1), ('number', 2), ('number', 3), ('number', 4), ('number', 5), ('number', 6), ('number', 7),
            ('number', 8), ('number', 9)]

def scan(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len([val for typ,val in verbs if val.lower() == word.lower()]) > 0 :
            result.extend([(typ, val) for typ,val in verbs if val == word])
        elif len([val for typ,val in directions if val.lower() == word.lower()]) > 0:
            result.extend([(typ, val) for typ,val in directions if val == word])
        elif len([val for typ,val in stop_words if val.lower() == word.lower()]) > 0:
            result.extend([(typ, val) for typ,val in stop_words if val == word])
        elif len([val for typ,val in nouns if val.lower() == word.lower()]) > 0:
            result.extend([(typ, val) for typ,val in nouns if val == word])
        elif convert_numbers(word) != None:
            result.extend([('number', convert_numbers(word))])
        else:
            result.append(('error',word))
    return result

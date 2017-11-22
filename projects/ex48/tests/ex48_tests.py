from nose.tools import *
from ex48 import lexicon
from ex48 import parser

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [
        ('direction','north'),
        ('direction','south'),
        ('direction','east')
    ])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb','go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat')
    ])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop_word','the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [
        ('stop_word', 'the'),
        ('stop_word', 'in'),
        ('stop_word', 'of')
    ])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun','bear')])
    result = lexicon.scan("bear princess door")
    assert_equal(result, [
        ('noun', 'bear'),
        ('noun', 'princess'),
        ('noun', 'door')
    ])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number',1234)])
    result = lexicon.scan("3 12345 123")
    assert_equal(result, [
        ('number', 3),
        ('number', 12345),
        ('number', 123)
    ])

def test_errors():
    assert_equal(lexicon.scan("ASDFSFEF"),[('error', 'ASDFSFEF')])
    result = lexicon.scan("bear IAS door")
    assert_equal(result, [
        ('noun', 'bear'),
        ('error', 'IAS'),
        ('noun', 'door')
    ])
def test_parse_sentence():
    pars = parser.Parser()
    assert_raises(parser.ParserError, pars.parse_sentence, [('stop_word', 'the'),('stop_word', 'the'), ('stop_word', 'the')])

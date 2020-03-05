from nose.tools import *
from ex48 import lexicon


def test_directions():
    assert_equal(lexicon.scan('north'), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east')
    ])


def test_verbs():
    assert_equal(lexicon.scan('go'), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat')
    ])


def test_stops():
    assert_equal(lexicon.scan('the'), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of')
    ])


def test_nouns():
    assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
    result = lexicon.scan("bear princess cabinet")
    assert_equal(result, [
        ('noun', 'bear'),
        ('noun', 'princess'),
        ('noun', 'cabinet')
    ])


def test_numbers():
    assert_equal(lexicon.scan('1'), [('number', 1)])
    result = lexicon.scan("1 2 3")
    assert_equal(result, [
        ('number', 1),
        ('number', 2),
        ('number', 3)
    ])


def test_errors():
    assert_equal(lexicon.scan('adad'), [('error', 'adad')])
    result = lexicon.scan("adad dada baba")
    assert_equal(result, [
        ('error', 'adad'),
        ('error', 'dada'),
        ('error', 'baba')
    ])

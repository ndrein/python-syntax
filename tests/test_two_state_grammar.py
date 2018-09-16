import pytest

from tests.character_not_in_alphabet import CharacterNotInAlphabet
from tests.grammar import Grammar

grammar = Grammar(states={1, 2}, start_state=1, accept_states={2}, alphabet={'a'}, transitions={(1, 'a'): 2})


def test_empty_string():
    assert grammar.tokenize('') == ('', '')


def test_single_character():
    assert grammar.tokenize('a') == ('a', '')


def test_invalid_character():
    with pytest.raises(CharacterNotInAlphabet):
        grammar.tokenize('b')


def test_two_characters():
    assert grammar.tokenize('aa') == ('a', 'a')

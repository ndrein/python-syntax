from enum import Enum

import pytest

from tests.character_not_in_alphabet import CharacterNotInAlphabet
from tests.grammar import Grammar, Token

TokenType = Enum('TokenType', 'A')

grammar = Grammar(states={1, 2}, start_state=1, accept_states={2}, alphabet={'a'}, transitions={(1, 'a'): 2},
                  accept_state_to_token_type={2: TokenType.A})


def test_empty_string():
    assert grammar.tokenize('') == (None, '')


def test_single_character():
    assert grammar.tokenize('a') == (Token(TokenType.A, 'a'), '')


def test_invalid_character():
    with pytest.raises(CharacterNotInAlphabet):
        grammar.tokenize('b')


def test_two_characters():
    assert grammar.tokenize('aa') == (Token(TokenType.A, 'a'), 'a')

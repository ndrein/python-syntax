from enum import Enum

import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.tokenizer import Tokenizer, Token

TokenType = Enum('TokenType', 'A')

grammar = Tokenizer(states={0, 1}, start_state=0, accept_states={1}, alphabet={'a'}, transitions={(0, 'a'): 1},
                    accept_state_to_token_type={1: TokenType.A})


def test_empty_string():
    assert grammar.munch('') == (None, '')


@pytest.mark.skip
def test_single_character():
    assert (Token(TokenType.A, 'a'), '') == grammar.munch('a')


def test_invalid_character():
    with pytest.raises(CharacterNotInAlphabet):
        grammar.munch('b')


@pytest.mark.skip
def test_two_characters():
    assert (Token(TokenType.A, 'a'), 'a') == grammar.munch('aa')

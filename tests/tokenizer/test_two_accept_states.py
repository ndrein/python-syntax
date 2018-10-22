from enum import Enum

import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.dfa import DFA, Token

TokenType = Enum('TokenType', ['A', 'B'])

tokenizer = DFA(start_state=0, accept_states={0, 1}, alphabet={'a'}, transitions={(0, 'a'): 1, (1, 'a'): 1})


def test_invalid_character():
    with pytest.raises(CharacterNotInAlphabet):
        tokenizer.traverse('b')


def test_second_accept_state():
    assert (Token(TokenType.B, 'a'), '') == tokenizer.traverse('a')
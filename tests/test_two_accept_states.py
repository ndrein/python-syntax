from enum import Enum

import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.dfa import DFA, Token

TokenType = Enum('TokenType', ['A', 'B'])

tokenizer = DFA(start_state=0, accept_states={0, 1}, alphabet={'a'}, transitions={(0, 'a'): 1, (1, 'a'): 1},
                accept_state_to_token_type={0: TokenType.A, 1: TokenType.B})


def test_invalid_character():
    with pytest.raises(CharacterNotInAlphabet):
        tokenizer.munch('b')


def test_second_accept_state():
    assert (Token(TokenType.B, 'a'), '') == tokenizer.munch('a')
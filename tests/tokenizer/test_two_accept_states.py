from enum import Enum

import pytest

from syntax.tokenizer import Tokenizer, InvalidCharacterException, Token

TokenType = Enum('TokenType', ['A', 'B'])

tokenizer = Tokenizer(start_state=0, accept_states={0, 1}, alphabet={'a'}, transitions={(0, 'a'): 1, (1, 'a'): 1},
                      accept_state_to_token_type={0: TokenType.A, 1: TokenType.B})


def test_invalid_character():
    with pytest.raises(InvalidCharacterException):
        tokenizer.munch('b')


def test_second_accept_state():
    assert Token(TokenType.A, 'a'), 1 == tokenizer.munch('a')

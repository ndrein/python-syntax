from enum import Enum

import pytest

from syntax.tokenizer import Tokenizer, Token


def test_empty_string_raises_error():
    tokenizer = Tokenizer({}, 0, set(), {})
    with pytest.raises(ValueError):
        tokenizer.tokenize('')


def test_empty_string_returns_valid_token():
    TokenType = Enum('TokenType', ['A'])
    tokenizer = Tokenizer({}, 0, {0}, {0: TokenType.A})
    assert [Token(TokenType.A, '')] == tokenizer.tokenize('')

from enum import Enum

import pytest

from syntax.tokenizer import Tokenizer, Token


def test_empty_string_raises_error():
    tokenizer = Tokenizer({}, 0, set(), {})
    with pytest.raises(ValueError):
        tokenizer.tokenize('')


def test_unexpected_character():
    with pytest.raises(ValueError):
        Tokenizer({}, 0, set(), {}).tokenize('a')


def test_two_tokens():
    TokenType = Enum('TokenType', ['A'])
    tokenizer = Tokenizer({(0, 'a'): 1}, 0, {1}, {1: TokenType.A})
    assert [Token(TokenType.A, 'a'), Token(TokenType.A, 'a')] == tokenizer.tokenize('aa')


def test_nonempty_string_gives_token_not_formed():
    with pytest.raises(ValueError):
        Tokenizer({(0, 'a'): 1}, 0, set(), {}).tokenize('a')

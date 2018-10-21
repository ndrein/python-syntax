from syntax.tokenizer import Tokenizer, Token

from enum import Enum

TokenType = Enum('TokenType', ['a'])
tokenizer = Tokenizer({0}, 0, {0}, {'a'}, {(0, 'a'): 0}, {0: TokenType.a})


def test_a():
    assert (Token(TokenType.a, 'a'), '') == tokenizer.munch('a')


def test_aa():
    assert (Token(TokenType.a, 'aa'), '') == tokenizer.munch('aa')

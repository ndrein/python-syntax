from syntax.grammar import Grammar, Token
from enum import Enum

TokenType = Enum('TokenType', ['A', 'B'])

grammar = Grammar({0, 1}, 0, {0, 1}, {'a', 'b'}, {(0, 'a'): 0, (0, 'b'): 1}, {0: TokenType.A, 1: TokenType.B})


def test_a():
    assert grammar.munch('a') == (Token(TokenType.A, 'a'), '')

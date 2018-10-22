from enum import Enum

import pytest

from syntax.dfa import DFA, Token

TokenType = Enum('TokenType', ['A', 'B'])

grammar = DFA(0, {0, 1}, {'a', 'b'}, {(0, 'a'): 0, (0, 'b'): 1})


@pytest.mark.skip
def test_a():
    assert grammar.traverse('a') == (Token(TokenType.A, 'a'), '')


@pytest.mark.skip
def test_aa():
    assert grammar.traverse('aa') == (Token(TokenType.A, 'aa'), '')

from syntax.dfa import DFA, Token
import pytest

from enum import Enum

TokenType = Enum('TokenType', ['A'])
tokenizer = DFA(start_state=0, accept_states={0}, alphabet={'a'}, transitions={(0, 'a'): 0})


def test_a():
    assert (Token(TokenType.A, 'a'), '') == tokenizer.munch('a')


@pytest.mark.skip
def test_aa():
    assert (Token(TokenType.A, 'aa'), '') == tokenizer.munch('aa')

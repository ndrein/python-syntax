from enum import Enum

from syntax.dfa import DFA

TokenType = Enum('TokenType', ['A'])
tokenizer = DFA(start_state=0, accept_states={0}, alphabet={'a'}, transitions={(0, 'a'): 0})


def test_a():
    assert (0, 1) == tokenizer.traverse('a')


def test_aa():
    assert (0, 2) == tokenizer.traverse('aa')

from enum import Enum

import pytest

from syntax.dfa import DFA

TokenType = Enum('TokenType', ['A'])
tokenizer = DFA(start_state=0, accept_states={0}, alphabet={'a'}, transitions={(0, 'a'): 0})


def test_a():
    assert (0, 1) == tokenizer.traverse('a')


@pytest.mark.skip
def test_aa():
    assert (0, 2) == tokenizer.traverse('aa')

from syntax.dfa import DFA
import pytest

tokenizer = DFA(start_state=0, accept_states=set(), alphabet={'a'}, transitions={(0, 'a'): 0},
                accept_state_to_token_type={})


def test_a():
    assert (None, 'a') == tokenizer.munch('a')

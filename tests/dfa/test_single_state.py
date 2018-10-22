from syntax.dfa import DFA

tokenizer = DFA(start_state=0, accept_states=set(), alphabet={'a'}, transitions={(0, 'a'): 0})


def test_a():
    assert None is tokenizer.traverse('a')

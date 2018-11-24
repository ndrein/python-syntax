from string import ascii_lowercase

from syntax.logic_dfa import logic_dfa


def _chain_lookups(d, start_state, s):
    """Starting from start_state, chain the lookups on d using the characters in s

    E.g. _chain_lookups(d, 0, 'ab') == d[d[0, 'a'], 'b']
    """
    if len(s) == 1:
        return d[start_state, s]

    return d[_chain_lookups(d, start_state, s[:-1]), s[-1]]


def test_literals():
    assert 1 == logic_dfa.transitions[0, 'a']
    assert 1 == logic_dfa.transitions[0, 'z']
    assert 1 == logic_dfa.transitions[logic_dfa.transitions[0, 'a'], 'b']
    assert 1 == _chain_lookups(logic_dfa.transitions, 0, ascii_lowercase)


def test_not():
    assert 4 == _chain_lookups(logic_dfa.transitions, 0, 'NOT')


def test_and():
    assert 7 == _chain_lookups(logic_dfa.transitions, 0, 'AND')


def test_or():
    assert 9 == _chain_lookups(logic_dfa.transitions, 0, 'OR')


def test_implies():
    assert 16 == _chain_lookups(logic_dfa.transitions, 0, 'IMPLIES')


def test_l_paren():
    assert 17 == logic_dfa.transitions[0, '(']


def test_r_paren():
    assert 18 == logic_dfa.transitions[0, ')']


def test_whitespace():
    assert 19 == logic_dfa.transitions[0, ' ']
    assert 19 == _chain_lookups(logic_dfa.transitions, 0, '  ')

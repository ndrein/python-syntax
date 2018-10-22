import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.dfa import DFA

grammar = DFA(start_state=1, accept_states=set(), alphabet=set(), transitions={})


def test_empty_string():
    assert (None, '') == grammar.munch('')


def test_invalid_symbol():
    with pytest.raises(CharacterNotInAlphabet):
        grammar.munch('a')

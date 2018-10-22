import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.dfa import DFA

dfa = DFA(start_state=0, accept_states=set(), alphabet=set(), transitions={})


def test_empty_string():
    assert None == dfa.traverse('')


def test_invalid_symbol():
    with pytest.raises(CharacterNotInAlphabet):
        dfa.traverse('a')

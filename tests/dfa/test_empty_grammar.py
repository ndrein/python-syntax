import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.tokenizer import Tokenizer

dfa = Tokenizer(start_state=0, accept_states=set(), alphabet=set(), transitions={})


def test_empty_string():
    assert None is dfa.traverse('')


def test_invalid_character():
    with pytest.raises(CharacterNotInAlphabet):
        dfa.traverse('a')

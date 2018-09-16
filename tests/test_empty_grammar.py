import pytest

from tests.grammar import Grammar
from tests.character_not_in_alphabet import CharacterNotInAlphabet

grammar = Grammar(states={1}, start_state=1, accept_states=set(), alphabet=set(), transitions={}, accept_state_to_token_type={})


def test_empty_string():
    assert grammar.tokenize('') == ('', '')


def test_invalid_symbol():
    with pytest.raises(CharacterNotInAlphabet):
        grammar.tokenize('a')

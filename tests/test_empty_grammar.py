import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.tokenizer import Tokenizer

grammar = Tokenizer(states={1}, start_state=1, accept_states=set(), alphabet=set(), transitions={},
                    accept_state_to_token_type={})


def test_empty_string():
    assert (None, '') == grammar.munch('')


def test_invalid_symbol():
    with pytest.raises(CharacterNotInAlphabet):
        grammar.munch('a')

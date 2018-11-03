import pytest

from syntax.tokenizer import Tokenizer

tokenizer = Tokenizer(transitions={}, start_state=0, accept_states=set(), accept_state_to_token_type={})


def test_empty_string():
    with pytest.raises(ValueError):
        tokenizer.tokenize('')


def test_invalid_character():
    with pytest.raises(ValueError):
        tokenizer.tokenize('a')

import pytest

from syntax.tokenizer import Tokenizer, TokenNotFormedException, InvalidCharacterException

tokenizer = Tokenizer(transitions={}, start_state=0, accept_states=set(), accept_state_to_token_type={})


def test_empty_string():
    with pytest.raises(TokenNotFormedException):
        tokenizer.munch('')


def test_invalid_character():
    with pytest.raises(InvalidCharacterException):
        tokenizer.munch('a')

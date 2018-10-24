import pytest

from syntax.tokenizer import Tokenizer, TokenNotFormedException, InvalidCharacterException

tokenizer = Tokenizer(start_state=0, accept_states=set(), alphabet=set(), transitions={}, accept_state_to_token_type={})


def test_empty_string():
    with pytest.raises(TokenNotFormedException):
        tokenizer.munch('')


def test_invalid_character():
    with pytest.raises(InvalidCharacterException):
        tokenizer.munch('a')

import pytest

from syntax.tokenizer import Tokenizer, InvalidCharacterException

tokenizer = Tokenizer(transitions={(0, '('): 1}, start_state=0, accept_states={1})


def test_empty_string():
    assert [] == tokenizer.tokenize('')


def test_invalid_character():
    with pytest.raises(InvalidCharacterException):
        tokenizer.tokenize('a')

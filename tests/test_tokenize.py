import pytest

from syntax.tokenizer import Tokenizer


def test_empty_string_raises_error():
    tokenizer = Tokenizer({}, 0, set(), {})
    with pytest.raises(ValueError):
        tokenizer.tokenize('')

# def test_empty_string_returns_empty_list():
#     tokenizer = Tokenizer({}, 0, set(), {})
#     assert [] == tokenizer.tokenize('')

# def test_empty_string_return():
#     pass

import pytest

from syntax.tokenizer import Tokenizer

tokenizer = Tokenizer(transitions={(0, 'a'): 0}, start_state=0, accept_states=set(), accept_state_to_token_type={})


def test_a():
    with pytest.raises(ValueError):
        tokenizer.tokenize('a')

from enum import Enum

import pytest

from syntax.character_not_in_alphabet import CharacterNotInAlphabet
from syntax.tokenizer import Tokenizer

TokenType = Enum('TokenType', ['A', 'B'])

tokenizer = Tokenizer(start_state=0, accept_states={0, 1}, alphabet={'a'}, transitions={(0, 'a'): 1, (1, 'a'): 1})


def test_invalid_character():
    with pytest.raises(CharacterNotInAlphabet):
        tokenizer.traverse('b')


def test_second_accept_state():
    assert (1, 1) == tokenizer.traverse('a')
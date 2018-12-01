from enum import Enum

import pytest

from syntax.tokenizer import Tokenizer, Token

A_TOKEN_TYPE = Enum('TokenType', ['A'])
AB_TOKEN_TYPE = Enum('TokenType', ['A', 'B'])


def test_empty_string_gives_no_tokens():
    assert [] == list(Tokenizer({}, 0, set(), {}).tokenize(''))


def test_unexpected_character():
    with pytest.raises(ValueError):
        list(Tokenizer({}, 0, set(), {}).tokenize('a'))


def test_accept_state_not_found():
    tokenizer = Tokenizer(transitions={(0, 'a'): 0}, start_state=0, accept_states=set(), accept_state_to_token_type={})
    with pytest.raises(ValueError):
        list(tokenizer.tokenize('a'))


def test_single_token():
    tokenizer = Tokenizer(transitions={(0, 'a'): 0}, start_state=0, accept_states={0},
                          accept_state_to_token_type={0: A_TOKEN_TYPE.A})
    assert [Token(A_TOKEN_TYPE.A, 'a')] == list(tokenizer.tokenize('a'))


def test_multi_char_token():
    tokenizer = Tokenizer(transitions={(0, 'a'): 0}, start_state=0, accept_states={0},
                          accept_state_to_token_type={0: A_TOKEN_TYPE.A})
    assert [Token(A_TOKEN_TYPE.A, 'aa')] == list(tokenizer.tokenize('aa'))


def test_second_accept_state():
    tokenizer = Tokenizer(transitions={(0, 'a'): 1, (1, 'a'): 1}, start_state=0, accept_states={0, 1},
                          accept_state_to_token_type={0: AB_TOKEN_TYPE.A, 1: AB_TOKEN_TYPE.B})
    assert [Token(AB_TOKEN_TYPE.B, 'a')] == list(tokenizer.tokenize('a'))


def test_munch_ends_after_nonempty_token():
    tokenizer = Tokenizer({(0, 'a'): 1, (1, 'a'): 2}, 0, {1}, {1: A_TOKEN_TYPE.A})
    assert [Token(A_TOKEN_TYPE.A, 'a'), Token(A_TOKEN_TYPE.A, 'a')] == list(tokenizer.tokenize('aa'))


def test_munch_ends_if_no_transition_exists():
    tokenizer = Tokenizer({(0, 'a'): 1}, 0, {1}, {1: A_TOKEN_TYPE.A})
    assert [Token(A_TOKEN_TYPE.A, 'a'), Token(A_TOKEN_TYPE.A, 'a')] == list(tokenizer.tokenize('aa'))


def test_two_different_tokens():
    tokenizer = Tokenizer({(0, 'a'): 1, (0, 'b'): 2}, 0, {1, 2}, {1: AB_TOKEN_TYPE.A, 2: AB_TOKEN_TYPE.B})
    assert [Token(AB_TOKEN_TYPE.A, 'a'), Token(AB_TOKEN_TYPE.B, 'b')] == list(tokenizer.tokenize('ab'))


def test_many_tokens():
    tokenizer = Tokenizer({(0, 'a'): 1}, 0, {1}, {1: A_TOKEN_TYPE.A})
    token = Token(A_TOKEN_TYPE.A, 'a')
    assert [token] * 1000 == list(tokenizer.tokenize('a' * 1000))

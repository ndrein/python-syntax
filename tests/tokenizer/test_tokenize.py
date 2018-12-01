from enum import Enum

import pytest

from syntax.tokenizer import Tokenizer, Token


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
    TokenType = Enum('TokenType', ['A'])
    tokenizer = Tokenizer(transitions={(0, 'a'): 0}, start_state=0, accept_states={0},
                          accept_state_to_token_type={0: TokenType.A})
    assert [Token(TokenType.A, 'a')] == list(tokenizer.tokenize('a'))


def test_multi_char_token():
    TokenType = Enum('TokenType', ['A'])
    tokenizer = Tokenizer(transitions={(0, 'a'): 0}, start_state=0, accept_states={0},
                          accept_state_to_token_type={0: TokenType.A})
    assert [Token(TokenType.A, 'aa')] == list(tokenizer.tokenize('aa'))


def test_second_accept_state():
    TokenType = Enum('TokenType', ['A', 'B'])
    tokenizer = Tokenizer(transitions={(0, 'a'): 1, (1, 'a'): 1}, start_state=0, accept_states={0, 1},
                          accept_state_to_token_type={0: TokenType.A, 1: TokenType.B})
    assert [Token(TokenType.B, 'a')] == list(tokenizer.tokenize('a'))


def test_munch_ends_after_nonempty_token():
    TokenType = Enum('TokenType', ['A'])
    tokenizer = Tokenizer({(0, 'a'): 1, (1, 'a'): 2}, 0, {1}, {1: TokenType.A})
    assert [Token(TokenType.A, 'a'), Token(TokenType.A, 'a')] == list(tokenizer.tokenize('aa'))


def test_munch_ends_if_no_transition_exists():
    TokenType = Enum('TokenType', ['A'])
    tokenizer = Tokenizer({(0, 'a'): 1}, 0, {1}, {1: TokenType.A})
    assert [Token(TokenType.A, 'a'), Token(TokenType.A, 'a')] == list(tokenizer.tokenize('aa'))


def test_two_different_tokens():
    TokenType = Enum('TokenType', ['A', 'B'])
    tokenizer = Tokenizer({(0, 'a'): 1, (0, 'b'): 2}, 0, {1, 2}, {1: TokenType.A, 2: TokenType.B})
    assert [Token(TokenType.A, 'a'), Token(TokenType.B, 'b')] == list(tokenizer.tokenize('ab'))


def test_many_tokens():
    TokenType = Enum('TokenType', ['A'])
    tokenizer = Tokenizer({(0, 'a'): 1}, 0, {1}, {1: TokenType.A})
    token = Token(TokenType.A, 'a')
    assert [token] * 1000 == list(tokenizer.tokenize('a' * 1000))

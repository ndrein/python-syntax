from enum import Enum

from syntax.tokenizer import Tokenizer, Token

TokenType = Enum('TokenType', ['A'])


def test_start_state_is_accept_state():
    tokenizer = Tokenizer({(0, 'a'): 1}, 0, {0}, {0: TokenType.A})
    assert Token(TokenType.A, ''), 0 == tokenizer.munch('')
    assert Token(TokenType.A, ''), 0 == tokenizer.munch('a')


def test_munch_ends_after_nonempty_token():
    tokenizer = Tokenizer({(0, 'a'): 1, (1, 'a'): 2}, 0, {1}, {1: TokenType.A})
    assert Token(TokenType.A, 'a'), 1 == tokenizer.munch('aa')

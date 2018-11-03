from enum import Enum

from syntax.tokenizer import Tokenizer, Token

TokenType = Enum('TokenType', ['A'])


def test_munch_ends_after_nonempty_token():
    tokenizer = Tokenizer({(0, 'a'): 1, (1, 'a'): 2}, 0, {1}, {1: TokenType.A})
    assert [Token(TokenType.A, 'a'), Token(TokenType.A, 'a')] == tokenizer.tokenize('aa')


def test_munch_ends_if_no_transition_exists():
    tokenizer = Tokenizer({(0, 'a'): 1}, 0, {1}, {1: TokenType.A})
    assert [Token(TokenType.A, 'a')] == tokenizer.tokenize('aa')

from enum import Enum

from syntax.tokenizer import Tokenizer, Token

TokenType = Enum('TokenType', ['A'])
tokenizer = Tokenizer(transitions={(0, 'a'): 0}, start_state=0, accept_states={0},
                      accept_state_to_token_type={0: TokenType.A})


def test_a():
    assert [Token(TokenType.A, 'a')] == tokenizer.tokenize('a')


def test_aa():
    assert [Token(TokenType.A, 'aa')] == tokenizer.tokenize('aa')
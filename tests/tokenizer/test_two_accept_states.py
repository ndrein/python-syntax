from enum import Enum

from syntax.tokenizer import Tokenizer, Token

TokenType = Enum('TokenType', ['A', 'B'])

tokenizer = Tokenizer(transitions={(0, 'a'): 1, (1, 'a'): 1}, start_state=0, accept_states={0, 1},
                      accept_state_to_token_type={0: TokenType.A, 1: TokenType.B})


def test_second_accept_state():
    assert [Token(TokenType.B, 'a')] == tokenizer.tokenize('a')

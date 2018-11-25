from syntax.logic_dfa import logic_dfa, TokenType
from syntax.tokenizer import Tokenizer, Token

tokenizer = Tokenizer(logic_dfa['transitions'], logic_dfa['start_state'], logic_dfa['accept_states'],
                      logic_dfa['accept_state_to_token_type'])


def test_space():
    assert [Token(TokenType.SPACE, ' ')] == tokenizer.tokenize(' ')


def test_literal():
    assert [Token(TokenType.LITERAL, 'a')] == tokenizer.tokenize('a')


def test_literal_and_operator():
    assert [Token(TokenType.LITERAL, 'a'), Token(TokenType.SPACE, ' ')] == tokenizer.tokenize('a ')


def test_lowercase_operators():
    not_ = Token(TokenType.LITERAL, 'not')
    space = Token(TokenType.SPACE, ' ')
    and_ = Token(TokenType.LITERAL, 'and')
    or_ = Token(TokenType.LITERAL, 'or')
    implies = Token(TokenType.LITERAL, 'implies')

    assert [not_, space, and_, space, or_, space, implies] == tokenizer.tokenize('not and or implies')

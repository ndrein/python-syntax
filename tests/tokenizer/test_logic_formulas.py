from syntax.tokenizer.logic_dfa import logic_dfa, TokenType
from syntax.tokenizer.tokenizer import Tokenizer, Token

tokenizer = Tokenizer(logic_dfa['transitions'], logic_dfa['start_state'], logic_dfa['accept_states'],
                      logic_dfa['accept_state_to_token_type'])


def test_space():
    assert [Token(TokenType.SPACE, ' ')] == list(tokenizer.tokenize(' '))


def test_literal():
    assert [Token(TokenType.LITERAL, 'a')] == list(tokenizer.tokenize('a'))


def test_literal_and_operator():
    assert [Token(TokenType.LITERAL, 'a'), Token(TokenType.SPACE, ' ')] == list(tokenizer.tokenize('a '))


def test_lowercase_operator_literals():
    not_ = Token(TokenType.LITERAL, 'not')
    space = Token(TokenType.SPACE, ' ')
    and_ = Token(TokenType.LITERAL, 'and')
    or_ = Token(TokenType.LITERAL, 'or')
    implies = Token(TokenType.LITERAL, 'implies')

    assert [not_, space, and_, space, or_, space, implies] == list(tokenizer.tokenize('not and or implies'))


def test_operators():
    not_ = Token(TokenType.NOT, 'NOT')
    space = Token(TokenType.SPACE, ' ')
    and_ = Token(TokenType.AND, 'AND')
    or_ = Token(TokenType.OR, 'OR')
    implies = Token(TokenType.IMPLIES, 'IMPLIES')

    assert [not_, space, and_, space, or_, space, implies] == list(tokenizer.tokenize('NOT AND OR IMPLIES'))


def test_lparen():
    assert [Token(TokenType.LPAREN, '(')] == list(tokenizer.tokenize('('))


def test_rparen():
    assert [Token(TokenType.RPAREN, ')')] == list(tokenizer.tokenize(')'))


def test_logical_formula():
    lparen = Token(TokenType.LPAREN, '(')
    p = Token(TokenType.LITERAL, 'p')
    space = Token(TokenType.SPACE, ' ')
    and_ = Token(TokenType.AND, 'AND')
    q = Token(TokenType.LITERAL, 'q')
    rparen = Token(TokenType.RPAREN, ')')
    implies = Token(TokenType.IMPLIES, 'IMPLIES')
    not_ = Token(TokenType.NOT, 'NOT')
    r = Token(TokenType.LITERAL, 'r')

    assert [lparen, p, space, and_, space, q, rparen, space, implies, space, lparen, not_, space, r, rparen] == \
           list(tokenizer.tokenize('(p AND q) IMPLIES (NOT r)'))

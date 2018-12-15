import pytest
from lark import Lark
from lark.exceptions import UnexpectedCharacters, ParseError

from syntax.logic_grammar import LOGIC_GRAMMAR

START = 'statement'

grammar = Lark(LOGIC_GRAMMAR, start=START)


def test_hello_world():
    Lark('''start: WORD "," WORD "!"

            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
            ''').parse('Hello, World!')


def test_parse_p():
    tree = grammar.parse('p')
    assert START == tree.data
    assert ['p'] == tree.children


def test_long_literal():
    s = 'aweoriquwpeoiuasdfnxcvn'
    assert [s] == grammar.parse(s).children


def test_unexpected_characters():
    for c in ('A', '-', '1'):
        with pytest.raises(UnexpectedCharacters):
            grammar.parse(c)


def test_space_gives_parse_error():
    with pytest.raises(ParseError):
        grammar.parse(' ')

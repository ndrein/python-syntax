from lark import Lark

from syntax.logic_grammar import LOGIC_GRAMMAR

START = 'start'


def test_hello_world():
    Lark('''start: WORD "," WORD "!"

            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
            ''').parse('Hello, World!')


def test_parse_logic_grammar():
    Lark(LOGIC_GRAMMAR)


def test_parse_p():
    tree = Lark(LOGIC_GRAMMAR).parse('p')
    assert START == tree.data

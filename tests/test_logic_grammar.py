from typing import Iterable

import pytest
from lark import Lark
from lark import Tree
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


def test_literal_with_whitespace():
    assert ['p'] == grammar.parse('  p ').children


def single_connective_test(root: Tree, rule_name: str, literals: Iterable[str]):
    rule_node = root.children[0]
    assert rule_name == rule_node.data
    for literal, statement in zip(literals, rule_node.children):
        assert literal == statement.children[0]


def test_not_without_whitespace():
    single_connective_test(grammar.parse('(NOTp)'), 'not', ['p'])


def test_not_with_whitespace():
    single_connective_test(grammar.parse('  (NOT p ) '), 'not', ['p'])


def test_double_negation():
    tree = grammar.parse('(NOT (NOT p))')
    not_node_1 = tree.children[0]
    assert 'not' == not_node_1.data
    single_connective_test(not_node_1.children[0], 'not', ['p'])


def test_or():
    single_connective_test(grammar.parse('(pORq)'), 'or', ['p', 'q'])


def test_or_and_not():
    tree = grammar.parse('(p OR (NOT q))')
    or_node = tree.children[0]
    assert 'or' == or_node.data
    assert ['p'] == or_node.children[0].children
    single_connective_test(or_node.children[1], 'not', ['q'])


def test_and():
    single_connective_test(grammar.parse('(p AND q)'), 'and', ['p', 'q'])


def test_and_or():
    tree = grammar.parse('((p OR q) AND r)')
    and_node = tree.children[0]
    assert 'and' == and_node.data
    single_connective_test(and_node.children[0], 'or', ['p', 'q'])
    assert ['r'] == and_node.children[1].children


def test_implies():
    single_connective_test(grammar.parse('(p IMPLIES q)'), 'implies', ['p', 'q'])


def test_iff():
    single_connective_test(grammar.parse('(p IFF q)'), 'iff', ('p', 'q'))

from typing import Iterable, Union
from typing import Sequence

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


def test_parse_literal():
    assert_matches('p', grammar.parse('p'))


def test_long_literal():
    s = 'aweoriquwpeoiuasdfnxcvn'
    assert_matches(s, grammar.parse(s))


def test_unexpected_characters():
    for c in ('A', '-', '1'):
        with pytest.raises(UnexpectedCharacters):
            grammar.parse(c)


def test_space_gives_parse_error():
    with pytest.raises(ParseError):
        grammar.parse(' ')


def test_literal_with_whitespace():
    assert_matches('p', grammar.parse('  p '))


def single_connective_test(root: Tree, rule_name: str, literals: Iterable[str]):
    rule_node = root.children[0]
    assert rule_name == rule_node.data
    for literal, statement in zip(literals, rule_node.children):
        assert literal == statement.children[0]


def test_not_without_whitespace():
    assert_matches(('not', 'p'), grammar.parse('(NOTp)'))


def test_not_with_whitespace():
    assert_matches(('not', 'p'), grammar.parse('  (NOT p ) '))


def test_double_negation():
    assert_matches(('not', ('not', 'p')), grammar.parse('(NOT (NOT p))'))


def test_or():
    assert_matches(('or', 'p', 'q'), grammar.parse('(p OR q)'))


def test_or_and_not():
    assert_matches(('or', 'p', ('not', 'q')), grammar.parse('(p OR (NOT q))'))


def test_and():
    assert_matches(('and', 'p', 'q'), grammar.parse('(p AND q)'))


def test_and_or():
    assert_matches(('and', ('or', 'p', 'q'), 'r'), grammar.parse('((p OR q) AND r)'))


def test_implies():
    assert_matches(('implies', 'p', 'q'), grammar.parse('(p IMPLIES q)'))


def test_iff():
    assert_matches(('iff', 'p', 'q'), grammar.parse('(p IFF q)'))


def assert_matches(target: Union[str, Sequence], statement: Tree):
    assert 1 == len(statement.children)

    if isinstance(target, str):
        assert [target] == statement.children
    else:
        connective_name = target[0]
        rule_node = statement.children[0]
        assert connective_name == rule_node.data

        for subtarget, child in zip(target[1:], rule_node.children):
            assert_matches(subtarget, child)


def test_and_or_not_implies_iff():
    assert_matches(('and', 'a', ('or', ('not', 'b'), ('implies', ('iff', 'c', 'd'), 'e'))),
                   grammar.parse('(a AND ((NOT b) OR ((c IFF d) IMPLIES e)))'))

from enum import Enum
from itertools import count
from string import ascii_lowercase

TokenType = Enum('TokenType', ['LITERAL', 'NOT', 'AND', 'OR', 'IMPLIES', 'LPAREN', 'RPAREN', 'WHITESPACE'])
LOGIC_DFA = {}
counter = count(0)

START = 0
LITERAL = 1
NOT_1 = 2
NOT_2 = 3
NOT_3 = 4

for a in ascii_lowercase:
    LOGIC_DFA[START, a] = LITERAL
    LOGIC_DFA[LITERAL, a] = LITERAL

LOGIC_DFA[START, 'N'] = NOT_1
LOGIC_DFA[NOT_1, 'O'] = NOT_2
LOGIC_DFA[NOT_2, 'T'] = NOT_3

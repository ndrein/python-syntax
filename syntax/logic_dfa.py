from enum import Enum
from itertools import count
from string import ascii_lowercase

TokenType = Enum('TokenType', ['LITERAL', 'NOT', 'AND', 'OR', 'IMPLIES', 'LPAREN', 'RPAREN', 'SPACE'])
LOGIC_DFA = {}
counter = count(0)

START = next(counter)
LITERAL = next(counter)
NOT_1 = next(counter)
NOT_2 = next(counter)
NOT_3 = next(counter)
AND_1 = next(counter)
AND_2 = next(counter)
AND_3 = next(counter)
OR_1 = next(counter)
OR_2 = next(counter)
IMPLIES_1 = next(counter)
IMPLIES_2 = next(counter)
IMPLIES_3 = next(counter)
IMPLIES_4 = next(counter)
IMPLIES_5 = next(counter)
IMPLIES_6 = next(counter)
IMPLIES_7 = next(counter)
LPAREN = next(counter)
RPAREN = next(counter)
SPACE = next(counter)

for a in ascii_lowercase:
    LOGIC_DFA[START, a] = LITERAL
    LOGIC_DFA[LITERAL, a] = LITERAL

LOGIC_DFA[START, 'N'] = NOT_1
LOGIC_DFA[NOT_1, 'O'] = NOT_2
LOGIC_DFA[NOT_2, 'T'] = NOT_3

LOGIC_DFA[START, 'A'] = AND_1
LOGIC_DFA[AND_1, 'N'] = AND_2
LOGIC_DFA[AND_2, 'D'] = AND_3

LOGIC_DFA[START, 'O'] = OR_1
LOGIC_DFA[OR_1, 'R'] = OR_2

LOGIC_DFA[START, 'I'] = IMPLIES_1
LOGIC_DFA[IMPLIES_1, 'M'] = IMPLIES_2
LOGIC_DFA[IMPLIES_2, 'P'] = IMPLIES_3
LOGIC_DFA[IMPLIES_3, 'L'] = IMPLIES_4
LOGIC_DFA[IMPLIES_4, 'I'] = IMPLIES_5
LOGIC_DFA[IMPLIES_5, 'E'] = IMPLIES_6
LOGIC_DFA[IMPLIES_6, 'S'] = IMPLIES_7

LOGIC_DFA[START, '('] = LPAREN

LOGIC_DFA[START, ')'] = RPAREN

LOGIC_DFA[START, ' '] = SPACE
LOGIC_DFA[SPACE, ' '] = SPACE

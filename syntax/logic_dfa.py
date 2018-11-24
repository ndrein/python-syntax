from enum import Enum
from itertools import count
from string import ascii_lowercase

TokenType = Enum('TokenType', ['LITERAL', 'NOT', 'AND', 'OR', 'IMPLIES', 'LPAREN', 'RPAREN', 'SPACE'])
LOGIC_DFA = {}
counter = count(0)

START = next(counter)
LITERAL = next(counter)
NOT = [next(counter) for _ in 'NOT']
AND = [next(counter) for _ in 'AND']
OR = [next(counter) for _ in 'OR']
IMPLIES = [next(counter) for _ in 'IMPLIES']
LPAREN = next(counter)
RPAREN = next(counter)
SPACE = next(counter)

for a in ascii_lowercase:
    LOGIC_DFA[START, a] = LITERAL
    LOGIC_DFA[LITERAL, a] = LITERAL

LOGIC_DFA[START, 'N'] = NOT[0]
LOGIC_DFA[NOT[0], 'O'] = NOT[1]
LOGIC_DFA[NOT[1], 'T'] = NOT[2]

LOGIC_DFA[START, 'A'] = AND[0]
LOGIC_DFA[AND[0], 'N'] = AND[1]
LOGIC_DFA[AND[1], 'D'] = AND[2]

LOGIC_DFA[START, 'O'] = OR[0]
LOGIC_DFA[OR[0], 'R'] = OR[1]

LOGIC_DFA[START, 'I'] = IMPLIES[0]
LOGIC_DFA[IMPLIES[0], 'M'] = IMPLIES[1]
LOGIC_DFA[IMPLIES[1], 'P'] = IMPLIES[2]
LOGIC_DFA[IMPLIES[2], 'L'] = IMPLIES[3]
LOGIC_DFA[IMPLIES[3], 'I'] = IMPLIES[4]
LOGIC_DFA[IMPLIES[4], 'E'] = IMPLIES[5]
LOGIC_DFA[IMPLIES[5], 'S'] = IMPLIES[6]

LOGIC_DFA[START, '('] = LPAREN

LOGIC_DFA[START, ')'] = RPAREN

LOGIC_DFA[START, ' '] = SPACE
LOGIC_DFA[SPACE, ' '] = SPACE

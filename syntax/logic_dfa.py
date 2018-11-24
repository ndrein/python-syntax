from enum import Enum
from itertools import count
from string import ascii_lowercase

TokenType = Enum('TokenType', ['LITERAL', 'NOT', 'AND', 'OR', 'IMPLIES', 'LPAREN', 'RPAREN', 'SPACE'])
logic_dfa = {}
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
    logic_dfa[START, a] = LITERAL
    logic_dfa[LITERAL, a] = LITERAL

logic_dfa[START, 'N'] = NOT[0]
logic_dfa[NOT[0], 'O'] = NOT[1]
logic_dfa[NOT[1], 'T'] = NOT[2]

logic_dfa[START, 'A'] = AND[0]
logic_dfa[AND[0], 'N'] = AND[1]
logic_dfa[AND[1], 'D'] = AND[2]

logic_dfa[START, 'O'] = OR[0]
logic_dfa[OR[0], 'R'] = OR[1]

logic_dfa[START, 'I'] = IMPLIES[0]
logic_dfa[IMPLIES[0], 'M'] = IMPLIES[1]
logic_dfa[IMPLIES[1], 'P'] = IMPLIES[2]
logic_dfa[IMPLIES[2], 'L'] = IMPLIES[3]
logic_dfa[IMPLIES[3], 'I'] = IMPLIES[4]
logic_dfa[IMPLIES[4], 'E'] = IMPLIES[5]
logic_dfa[IMPLIES[5], 'S'] = IMPLIES[6]

logic_dfa[START, '('] = LPAREN

logic_dfa[START, ')'] = RPAREN

logic_dfa[START, ' '] = SPACE
logic_dfa[SPACE, ' '] = SPACE

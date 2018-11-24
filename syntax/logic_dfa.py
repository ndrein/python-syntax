from enum import Enum
from itertools import count
from string import ascii_lowercase

TokenType = Enum('TokenType', ['LITERAL', 'NOT', 'AND', 'OR', 'IMPLIES', 'LPAREN', 'RPAREN', 'SPACE'])
transitions = {}
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
    transitions[START, a] = LITERAL
    transitions[LITERAL, a] = LITERAL

transitions[START, 'N'] = NOT[0]
transitions[NOT[0], 'O'] = NOT[1]
transitions[NOT[1], 'T'] = NOT[2]

transitions[START, 'A'] = AND[0]
transitions[AND[0], 'N'] = AND[1]
transitions[AND[1], 'D'] = AND[2]

transitions[START, 'O'] = OR[0]
transitions[OR[0], 'R'] = OR[1]

transitions[START, 'I'] = IMPLIES[0]
transitions[IMPLIES[0], 'M'] = IMPLIES[1]
transitions[IMPLIES[1], 'P'] = IMPLIES[2]
transitions[IMPLIES[2], 'L'] = IMPLIES[3]
transitions[IMPLIES[3], 'I'] = IMPLIES[4]
transitions[IMPLIES[4], 'E'] = IMPLIES[5]
transitions[IMPLIES[5], 'S'] = IMPLIES[6]

transitions[START, '('] = LPAREN

transitions[START, ')'] = RPAREN

transitions[START, ' '] = SPACE
transitions[SPACE, ' '] = SPACE

#
# def get_logic_dfa():
#     return transitions, START, {LITERAL, NOT[-1], AND[-1], OR[-1], IMPLIES[-1], LPAREN, RPAREN, SPACE},
# {LITERAL: TokenType.LITERAL, NOT[-1]: TokenType.NOT, AND[-]}

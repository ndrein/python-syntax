from enum import Enum
from itertools import count
from string import ascii_lowercase

TokenType = Enum('TokenType', ['LITERAL', 'NOT', 'AND', 'OR', 'IMPLIES', 'LPAREN', 'RPAREN', 'SPACE'])
_transitions = {}
_counter = count(0)

START = next(_counter)
LITERAL = next(_counter)
NOT = [next(_counter) for _ in 'NOT']
AND = [next(_counter) for _ in 'AND']
OR = [next(_counter) for _ in 'OR']
IMPLIES = [next(_counter) for _ in 'IMPLIES']
LPAREN = next(_counter)
RPAREN = next(_counter)
SPACE = next(_counter)

for a in ascii_lowercase:
    _transitions[START, a] = LITERAL
    _transitions[LITERAL, a] = LITERAL

_transitions[START, 'N'] = NOT[0]
_transitions[NOT[0], 'O'] = NOT[1]
_transitions[NOT[1], 'T'] = NOT[2]

_transitions[START, 'A'] = AND[0]
_transitions[AND[0], 'N'] = AND[1]
_transitions[AND[1], 'D'] = AND[2]

_transitions[START, 'O'] = OR[0]
_transitions[OR[0], 'R'] = OR[1]

_transitions[START, 'I'] = IMPLIES[0]
_transitions[IMPLIES[0], 'M'] = IMPLIES[1]
_transitions[IMPLIES[1], 'P'] = IMPLIES[2]
_transitions[IMPLIES[2], 'L'] = IMPLIES[3]
_transitions[IMPLIES[3], 'I'] = IMPLIES[4]
_transitions[IMPLIES[4], 'E'] = IMPLIES[5]
_transitions[IMPLIES[5], 'S'] = IMPLIES[6]

_transitions[START, '('] = LPAREN

_transitions[START, ')'] = RPAREN

_transitions[START, ' '] = SPACE
_transitions[SPACE, ' '] = SPACE

logic_dfa = {'transitions': _transitions,
             'start_state': START,
             'accept_states': {LITERAL, NOT[-1], AND[-1], OR[-1], IMPLIES[-1], LPAREN, RPAREN, SPACE},
             'accept_state_to_token_type': {LITERAL: TokenType.LITERAL, NOT[-1]: TokenType.NOT, AND[-1]: TokenType.AND,
                                            OR[-1]: TokenType.OR,
                                            IMPLIES[-1]: TokenType.IMPLIES, LPAREN: TokenType.LPAREN,
                                            RPAREN: TokenType.RPAREN,
                                            SPACE: TokenType.SPACE}}

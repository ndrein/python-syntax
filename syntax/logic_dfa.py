from enum import Enum
from string import ascii_lowercase

TokenType = Enum('TokenType', ['LITERAL', 'NOT', 'AND', 'OR', 'IMPLIES', 'LPAREN', 'RPAREN', 'WHITESPACE'])

LOGIC_DFA = {}

for a in ascii_lowercase:
    LOGIC_DFA[0, a] = 1
    LOGIC_DFA[1, a] = 1

LOGIC_DFA[0, 'N'] = 2
LOGIC_DFA[2, 'O'] = 3
LOGIC_DFA[3, 'T'] = 4

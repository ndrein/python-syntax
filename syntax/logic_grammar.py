LOGIC_GRAMMAR = '''
start: LITERAL
         | not
         | or
         | and
         | implies
         | iff
LITERAL: /[a-z]+/
not: "(NOT" start ")"
or: "(" start "OR" start ")"
and: "(" start "AND" start ")"
implies: "(" start "IMPLIES" start ")"
iff: "(" start "IFF" start ")"

%import common.WS
%ignore WS
'''

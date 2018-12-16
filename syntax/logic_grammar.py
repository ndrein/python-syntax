LOGIC_GRAMMAR = '''
statement: LITERAL
         | not
         | or
         | and
         | implies
         | iff
LITERAL: /[a-z]+/
not: "(NOT" statement ")"
or: "(" statement "OR" statement ")"
and: "(" statement "AND" statement ")"
implies: "(" statement "IMPLIES" statement ")"
iff: "(" statement "IFF" statement ")"

%import common.WS
%ignore WS
'''

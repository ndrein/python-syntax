LOGIC_GRAMMAR = '''
statement: LITERAL
         | not
         | or
         | and
LITERAL: /[a-z]+/
not: "(NOT" statement ")"
or: "(" statement "OR" statement ")"
and: "(" statement "AND" statement ")"

%import common.WS
%ignore WS
'''

LOGIC_GRAMMAR = '''
statement: LITERAL
         | not
         | or
LITERAL: /[a-z]+/
not: "(NOT" statement ")"
or: "(" statement "OR" statement ")"

%import common.WS
%ignore WS
'''

from collections import namedtuple
from syntax.dfa import DFA

from syntax.character_not_in_alphabet import CharacterNotInAlphabet

Token = namedtuple('Token', ['TokenType', 's'])


class Tokenizer:
    def __init__(self, dfa, state_to_token_type):
        pass

    def munch(self, s):
        state = self.start_state

        for c in s:
            if c not in self.alphabet:
                raise CharacterNotInAlphabet

            state = self.transitions[state, c]

        if state in self.accept_states:
            return Token(self.accept_state_to_token_type[state], s), ''

        return None, s

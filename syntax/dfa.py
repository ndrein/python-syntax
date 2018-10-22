from collections import namedtuple

from syntax.character_not_in_alphabet import CharacterNotInAlphabet

Token = namedtuple('Token', ['TokenType', 's'])


class DFA:
    def __init__(self, start_state, accept_states, alphabet, transitions, accept_state_to_token_type):
        self.start_state = start_state
        self.accept_states = accept_states
        self.alphabet = alphabet
        self.transitions = transitions
        self.accept_state_to_token_type = accept_state_to_token_type

    def munch(self, s):
        state = self.start_state

        for c in s:
            if c not in self.alphabet:
                raise CharacterNotInAlphabet

            state = self.transitions[state, c]

        if state in self.accept_states:
            return Token(self.accept_state_to_token_type[state], s), ''

        return None, s

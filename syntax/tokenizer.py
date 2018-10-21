from collections import namedtuple

from syntax.character_not_in_alphabet import CharacterNotInAlphabet

Token = namedtuple('Token', ['TokenType', 's'])


class Tokenizer:
    def __init__(self, states, start_state, accept_states, alphabet, transitions, accept_state_to_token_type):
        self.alphabet = alphabet
        self.accept_state_to_token_type = accept_state_to_token_type
        self.start_state = start_state
        self.transitions = transitions
        self.accept_states = accept_states

    def munch(self, s):
        state = self.start_state
        for char in s:
            if char not in self.alphabet:
                raise CharacterNotInAlphabet

            state = self.transitions[state, char]

        # if not set(s).issubset(self.alphabet):
        #     raise CharacterNotInAlphabet

        if s == '':
            return None, ''
        elif self.start_state not in self.accept_states:
            return None
        else:
            return Token(self.accept_state_to_token_type[self.start_state], s), ''

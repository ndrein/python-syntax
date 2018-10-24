from collections import namedtuple

from syntax.character_not_in_alphabet import CharacterNotInAlphabet

Token = namedtuple('Token', ['TokenType', 's'])


class Tokenizer:
    def __init__(self, start_state, accept_states, alphabet, transitions):
        self.start_state = start_state
        self.accept_states = accept_states
        self.alphabet = alphabet
        self.transitions = transitions

    def traverse(self, s):
        state = self.start_state
        num_processed = 0

        for c in s:
            num_processed += 1

            if c not in self.alphabet:
                raise CharacterNotInAlphabet

            state = self.transitions[state, c]

        if state in self.accept_states:
            return state, num_processed

        return None

from collections import namedtuple

Token = namedtuple('Token', ['tokentype', 's'])


class Tokenizer:
    def __init__(self, start_state, accept_states, alphabet, transitions, accept_state_to_token_type):
        self.start_state = start_state
        self.accept_states = accept_states
        self.alphabet = alphabet
        self.transitions = transitions
        self.accept_state_to_token_type = accept_state_to_token_type

    def munch(self, s):
        state = self.start_state
        num_processed = 0

        for c in s:
            num_processed += 1

            if c not in self.alphabet:
                raise InvalidCharacterException

            state = self.transitions[state, c]

        if state in self.accept_states:
            return Token(self.accept_state_to_token_type[state], s), num_processed

        raise TokenNotFormedException


class TokenNotFormedException(Exception):
    pass


class InvalidCharacterException(Exception):
    pass

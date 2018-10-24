from collections import namedtuple

Token = namedtuple('Token', ['tokenType', 's'])


class Tokenizer:
    def __init__(self, transitions, start_state, accept_states, accept_state_to_token_type):
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions
        self.accept_state_to_token_type = accept_state_to_token_type

    def munch(self, s):
        state = self.start_state
        num_processed = 0

        for c in s:
            num_processed += 1

            try:
                state = self.transitions[state, c]
            except KeyError:
                raise InvalidCharacterException

        if state in self.accept_states:
            return Token(self.accept_state_to_token_type[state], s), num_processed

        raise TokenNotFormedException


class TokenNotFormedException(Exception):
    pass


class InvalidCharacterException(Exception):
    pass

from collections import namedtuple

Token = namedtuple('Token', ['tokenType', 's'])


class Tokenizer:
    def __init__(self, transitions, start_state, accept_states, accept_state_to_token_type):
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions
        self.accept_state_to_token_type = accept_state_to_token_type

    def munch(self, s):
        """
        Munch characters from s until an accept state is reached.
        Then, continue to munch while the next characters transition to accept states.

        :return: Token, num of characters processed
        :raises UnexpectedCharacterException if a character is encountered that leads to an invalid transition
        :raises TokenNotFormedException if an accept state is not reached
        """
        state = self.start_state
        num_processed = 0

        for c in s:
            num_processed += 1

            try:
                state = self.transitions[state, c]
            except KeyError:
                raise UnexpectedCharacterException

        if state in self.accept_states:
            return Token(self.accept_state_to_token_type[state], s), num_processed

        raise TokenNotFormedException

    def tokenize(self, s):
        """
        :return: list of Tokens
        :raises UnexpectedCharacterException if a character is encountered that leads to an invalid transition
        :raises TokenNotFormedException if an accept state is not reached
        """
        pass


class TokenNotFormedException(Exception):
    pass


class UnexpectedCharacterException(Exception):
    pass

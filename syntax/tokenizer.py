from collections import namedtuple

Token = namedtuple('Token', ['tokenType', 's'])


class Tokenizer:
    def __init__(self, transitions, start_state, accept_states, accept_state_to_token_type):
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions
        self.accept_state_to_token_type = accept_state_to_token_type

    def _munch(self, s):
        """
        Munch characters from s until an accept state is reached.
        Then, continue to munch while the next characters transition to accept states.

        :return: Token, num of characters processed
        :raises UnexpectedCharacterException if a character is encountered that leads to an invalid transition
        :raises TokenNotFormedException if an accept state is not reached
        """
        num_processed, state = self._process_chars(s, self.start_state)

        if state in self.accept_states:
            return Token(self.accept_state_to_token_type[state], s[:num_processed]), num_processed

        raise TokenNotFormedException

    def _process_chars(self, s, state):
        num_processed = 0

        for c in s:
            try:
                state = self.transitions[state, c]
            except KeyError:
                if state in self.accept_states:
                    break

                raise UnexpectedCharacterException

            num_processed += 1

        return state, num_processed

    def tokenize(self, s):
        """
        :return: list of Tokens
        :raises ValueError if the input could not be tokenized
        """
        try:
            return [self._munch(s)[0]]
        except (TokenNotFormedException, UnexpectedCharacterException):
            raise ValueError


class TokenNotFormedException(Exception):
    pass


class UnexpectedCharacterException(Exception):
    pass

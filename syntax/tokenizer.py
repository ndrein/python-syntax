from collections import namedtuple

from syntax.dfa import Dfa, UnexpectedCharacterException

Token = namedtuple('Token', ['tokenType', 's'])


class Tokenizer:
    def __init__(self, transitions, start_state, accept_states, accept_state_to_token_type):
        self.dfa = Dfa(transitions, start_state, accept_states)
        self.accept_states = accept_states
        self.accept_state_to_token_type = accept_state_to_token_type

    def tokenize(self, s):
        """
        Munch characters from s until an accept state is reached.
        Then, continue to munch while the next characters transition to accept states.
        If a new accept state can't be reached, emit a token

        :return: list of Token
        :raises: ValueError if a Token can't be formed from some characters
        """
        try:
            index = 0

            while index < len(s):
                token, num_processed = self._munch(s[index:])
                index += num_processed

                yield token
        except (TokenNotFormedException, UnexpectedCharacterException):
            raise ValueError

    def _munch(self, s):
        state, num_processed = self.dfa.process(s)

        if state in self.accept_states:
            return Token(self.accept_state_to_token_type[state], s[:num_processed]), num_processed

        raise TokenNotFormedException


class TokenNotFormedException(Exception):
    pass

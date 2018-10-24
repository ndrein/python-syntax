from collections import namedtuple

Token = namedtuple('Token', ['TokenType', 's'])


class Tokenizer:
    def __init__(self, transitions, start_state, accept_states):
        pass

    def tokenize(self, s):
        for _ in s:
            raise InvalidCharacterException

        return []


class InvalidCharacterException(Exception):
    pass

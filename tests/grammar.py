from collections import namedtuple

from tests.character_not_in_alphabet import CharacterNotInAlphabet

Token = namedtuple('Token', ['TokenType', 's'])


class Grammar:
    def __init__(self, states, start_state, accept_states, alphabet, transitions, accept_state_to_token_type):
        self.alphabet = alphabet
        self.accept_state_to_token_type = accept_state_to_token_type

    def tokenize(self, s):
        if s == '':
            return None, ''
        elif self.alphabet == set():
            raise CharacterNotInAlphabet
        elif set(s) != self.alphabet:
            raise CharacterNotInAlphabet
        else:
            return Token(self.accept_state_to_token_type[2], [0]), s[1:]

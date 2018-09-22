from collections import namedtuple

from syntax.character_not_in_alphabet import CharacterNotInAlphabet

Token = namedtuple('Token', ['TokenType', 's'])


class Grammar:
    def __init__(self, states, start_state, accept_states, alphabet, transitions, accept_state_to_token_type):
        self.alphabet = alphabet
        self.accept_state_to_token_type = accept_state_to_token_type
        self.start_state = start_state
        self.transitions = transitions

    def tokenize(self, s):
        if s == '':
            return None, ''
        elif not set(s).issubset(self.alphabet):
            raise CharacterNotInAlphabet
        else:
            return Token(self.accept_state_to_token_type[self.transitions[(self.start_state, s[0])]], s[0]), s[1:]

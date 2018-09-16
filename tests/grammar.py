from tests.character_not_in_alphabet import CharacterNotInAlphabet


class Grammar:
    def __init__(self, states, start_state, accept_states, alphabet, transitions, accept_state_to_token_type):
        self.alphabet = alphabet

    def tokenize(self, s):
        if s == '':
            return '', ''
        elif self.alphabet == set():
            raise CharacterNotInAlphabet
        elif set(s) != self.alphabet:
            raise CharacterNotInAlphabet
        else:
            return s[0], s[1:]

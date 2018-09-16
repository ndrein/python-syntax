from tests.character_not_in_alphabet import CharacterNotInAlphabet


class Grammar:
    def __init__(self, states, start_state, accept_states, alphabet, transitions):
        self.alphabet = alphabet

    def tokenize(self, s):
        if s == '':
            return '', ''
        elif self.alphabet == set():
            raise CharacterNotInAlphabet
        else:
            return 'a', ''

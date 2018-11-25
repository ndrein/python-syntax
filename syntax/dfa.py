class Dfa:
    def __init__(self, transitions, start_state, accept_states):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def process(self, s):
        """
        Traverse the Dfa by processing chars in s.
        If an accept state was encountered and no transition exists to an accept state immediately after, return

        :return: final state, number of characters processed
        :raises: UnexpectedCharacterException
        """
        # TODO: use inner class, or reduce method size
        state = self.start_state
        num_processed = 0
        found_accept_state = False

        for c in s:
            if (state, c) in self.transitions:
                next_state = self.transitions[state, c]

                if found_accept_state and next_state not in self.accept_states:
                    break
                state = self.transitions[state, c]
                if state in self.accept_states:
                    found_accept_state = True
            else:
                if state in self.accept_states:
                    break

                raise UnexpectedCharacterException

            num_processed += 1

        return state, num_processed


class UnexpectedCharacterException(Exception):
    pass

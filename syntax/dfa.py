from collections import namedtuple

Dfa = namedtuple('Dfa', ['transitions', 'start_state', 'accept_states', 'accept_state_to_token_type'])

from syntax.logic_dfa import logic_dfa
from syntax.tokenizer import Tokenizer


def test_simple_formula():
    tokenizer = Tokenizer(logic_dfa.transitions, logic_dfa.start_state, logic_dfa.accept_states,
                          logic_dfa.accept_state_to_token_type)

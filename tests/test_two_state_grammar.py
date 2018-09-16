from tests.grammar import Grammar

grammar = Grammar(states={1, 2}, start_state=1, accept_states={2}, alphabet={'a'}, transitions={(1, 'a'): 2})


def test_empty_string():
    assert grammar.tokenize('') == ('', '')


def test_single_character():
    assert grammar.tokenize('a') == ('a', '')

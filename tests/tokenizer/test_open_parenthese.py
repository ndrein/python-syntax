from syntax.tokenizer import Tokenizer


def test_empty_string():
    tokenizer = Tokenizer(transitions={(0, '('): 1}, start_state=0, accept_states={1})
    assert [] == tokenizer.tokenize('')

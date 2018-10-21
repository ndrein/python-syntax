from syntax.tokenizer import Tokenizer

tokenizer = Tokenizer({0}, 0, set(), {'a'}, {(0, 'a'): 0}, {})


def test_a():
    assert None is tokenizer.munch('a')

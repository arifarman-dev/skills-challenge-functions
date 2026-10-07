from lib.count_words import *
# Given a string of 0 words, return 0
def test_0_words_returns_0():
    test_text = count_words("")
    assert test_text == 0

# Given a string of 4 words, return 4
def test_0_words_returns_0():
    test_text = count_words("one two three four")
    assert test_text == 4

# Given a string of 5 words, return 5
def test_0_words_returns_0():
    test_text = count_words("one two three four five")
    assert test_text == 5
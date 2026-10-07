from lib.make_snippet import *

def test_make_snippet_returns_5():
    test_string = make_snippet("One two three four five six")
    assert test_string == "One two three four five..."
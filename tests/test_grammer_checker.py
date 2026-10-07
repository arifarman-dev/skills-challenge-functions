from lib.grammar_checker import *

def test_no_text_given():
    result = grammar_checker("")
    assert result == "No text"

def test_without_capital_without_punctuation():
    result = grammar_checker("""this does not start with a capital letter
    and does not end on an appropriate punctuation mark""")
    assert result == False

def test_with_capital_with_punctuation():
    result = grammar_checker("""This starts with a capital letter and ends
    on an appropriate punctuation mark!""")
    assert result == True

def test_with_capital_with_punctuation():
    result = grammar_checker("""This does start with a capital letter but
    does not end on an appropriate punctuation mark""")
    assert result == False

def test_without_capital_with_punctuation():
    result = grammar_checker("""this does not end with a capital letter
    but does end on an appropriate punctuation mark!""")
    assert result == False
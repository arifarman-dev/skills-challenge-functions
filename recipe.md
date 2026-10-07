# Single-Function Programs Design Recipe


## 1 Describe the problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


## 2 Design the Function Signiture
```python
def reading_time_estimate(text):
    # Parameters:
    #   text: a string of words
    # Return:
    #   estimated time: total number of items in the list/60 seconds
    pass
```


## Create Examples as Tests
```python
# Given an empty text return 0 seconds
# def test_empty_text_returns_0_seconds():
#     estimated_time = len(word_list)/200
#     returns estimated_time
#     assert estimated_time == 0

# Given text, return the estimated time
# def test_200_words_returns_1():
#     estimated_time = len(word_list)/200
#     returns estimated_time
#     assert estimated_time == 0
```

## 1 Describe the problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.


## 2 Design the Function Signiture
```python
def grammar_check(text):
    # Parameter:
    #   text: a string of words
    # Return:
    #   Boolean
    pass
```


## Create Examples as Tests
```python
"""
Empty string should return "No text"
"""

"""
Given a text without capital letter at the start and without an Appropriate punctuation mark at the end return False
"""
"this does not start with a capital letter and does not end on an appropriate punctuation mark"

"""
Given a text with a capital letter at the start and an appropriate Punctuation mark at the end return True
"""
"This starts with a capital letter and ends on an appropriate punctuation mark!"

"""
Given a text with capital letter at the start and no appropriate Punctuation mark at the end return False
"""
"This does start with a capital letter but does not end on an appropriate punctuation mark"

"""
Given a text without a capital letter at the start but ends with an appropriate punctuation mark return False
"""
"this does not end with a capital letter but does end on an appropriate punctuation mark!"
```
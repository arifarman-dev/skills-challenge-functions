def grammar_checker(text):
    appropriate_ending_punctuation = [".", "...", "!", "?", "!?"]
    if text == "":
        return "No text"
    if text[0] == text[0].upper() and text[-1] in appropriate_ending_punctuation:
        return True
    else:
        return False
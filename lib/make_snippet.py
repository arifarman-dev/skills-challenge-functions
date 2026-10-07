def make_snippet(string):
    if len(string.split()) > 5:
        five_words = string.split()[:5]
        return f"{" ".join(five_words)}..."
    else:
        return f"{string}"
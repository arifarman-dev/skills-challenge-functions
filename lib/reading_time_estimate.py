def reading_time_estimate(text):
    words = text.split()
    estimated_time = len(words)/200
    return estimated_time
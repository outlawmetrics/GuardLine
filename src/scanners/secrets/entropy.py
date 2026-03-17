import math

def calculate_entropy(text):
    if not text:
        return 0.0

    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1

    length = len(text)
    entropy = 0.0

    for count in char_counts.values():
        frequency = count / length
        entropy = entropy - frequency * math.log2(frequency)

    return entropy


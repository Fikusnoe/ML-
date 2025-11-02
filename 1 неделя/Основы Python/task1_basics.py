def count_vowels(text):
    letters = 'aeiou'
    count = 0

    text_lower = text.lower()
    for char in text_lower:
        if char in letters:
            count += 1
    return count
def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=lambda w: int(''.join(filter(str.isdigit, w))))

    return ' '.join(sorted_words)

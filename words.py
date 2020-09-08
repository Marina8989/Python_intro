words = ['hello', 'I', 'love', 'python', 'ee']


def print_upper_words(l):
    """Print each word from the list on a new line and in all uppercase"""
    for word in words:
        if word.startswith('e'):
            print(word.upper())


print(print_upper_words(words))
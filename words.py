words = ['hello', 'I', 'love', 'python', 'ee']


def print_upper_words(l):
    """Print each word from the list on a new line and in all uppercase

    >>>print_upper_words(['hello', 'I', 'love', 'python', 'ee'])
    HELLO
    I
    LOVE
    PYTHON
    EE
    """
    for word in words:
        if word.startswith('e'):
            print(word.upper())


print(print_upper_words(words))


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercase, if starts with one of given
        >>>print_upper_words3(["eagle", "edward", "Alfred", "zope"], must_start_with=["A", "E"])
        ...and
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
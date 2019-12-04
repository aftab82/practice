def is_unique(s):
    previous = None
    for letter in sorted(s):
        if letter == previous:
            return False
        previous = letter
    return True

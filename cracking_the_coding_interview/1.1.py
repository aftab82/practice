def is_unique(s):
    seen = []
    for letter in s:
        if letter in seen:
            return False
        seen.append(letter)
    return True

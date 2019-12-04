def replace_spaces(s):
    r = []
    for letter in s:
        if letter == ' ':
            r.append('%20')
        else: 
            r.append(letter)
    return r.join('')

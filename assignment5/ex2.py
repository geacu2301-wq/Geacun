def hexadecimal_format(color):
    if len(color) != 7:
        return False
    if color[0] != '#':
        return False
    for char in color[1:]:
        if not char.isdigit() and char.lower() not in 'abcdef':
            return False
    return True

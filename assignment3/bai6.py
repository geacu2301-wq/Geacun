def middle(line):
    n = len(line)
    m = n // 2
    if n % 2 == 0:
        return line[m-1:m+1]
    else:
        return line[m]        
def find_keyword_on_lines(bai2, keyword):
    result = []
    with open(bai2, 'r') as file:
        for index, line in enumerate(file, start=1):
            if keyword in line:
                result.append(index)
    return result
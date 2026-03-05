def course_university(code):
    if len (code) not in (5,6) :
        return False
    letters = code[:-3]
    digit = code[-3:]
    if not letters.isalpha() or not digit.isdigit():
        return False
    if not digit.isdigit():
        return False
    return True    
    
import re
def phone_number(s):
    pattern = r'(\+84\d+|\b\d{10}\b)'
    return re.sub(pattern, "[REDACTED]", s)

import re
def sum_number(s):
    number=re.findall(r'\d+',s)
    total=0
    for num in number:
        total+=int(num)
    return total
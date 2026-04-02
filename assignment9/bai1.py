def count_lines(bai1):
    count = 0
    with open(bai1, 'r') as file:
        for line in file:
            if line.strip() != "": 
                count += 1
    return count
        

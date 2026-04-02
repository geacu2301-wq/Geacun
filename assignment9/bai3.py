def average_score(bai3):
    total = 0
    count = 0
    with open(bai3, 'r') as file:
        for line in file:
            if line.strip() == "":
                continue 
            else:
                bai3, score = line.strip().split(',')
                total += float(score)
                count += 1
    if count == 0:
        return 0
    else:
        return total / count
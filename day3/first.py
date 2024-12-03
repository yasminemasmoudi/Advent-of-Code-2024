import re

sum_mul = 0

with open("input.txt") as file:
    lines = [line.strip() for line in file if line.strip()]
    # Regex pattern to match valid mul(X,Y) instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            x, y = int(match[0]), int(match[1])
            sum_mul += x * y
            
print(sum_mul)

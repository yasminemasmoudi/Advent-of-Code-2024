import re

total_sum = 0
enabled = True

with open("input.txt") as file:
    lines = [line.strip() for line in file if line.strip()]
    
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'  
    dont_pattern = r"don't\(\)"

    for line in lines:
        index = 0
        while index < len(line):
            if line[index:index+4] == "do()":
                enabled = True
                index += 4  
            
            elif line[index:index+7] == "don't()":
                enabled = False
                index += 7  
            
            elif enabled:
                mul_match = re.match(pattern, line[index:])
                if mul_match:
                    x, y = int(mul_match.group(1)), int(mul_match.group(2))
                    total_sum += x * y
                    index += len(mul_match.group(0))  
                else:
                    index += 1  
            else:
                index += 1  

print(total_sum)

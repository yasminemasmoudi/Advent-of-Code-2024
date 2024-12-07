from itertools import product

with open("input.txt") as file:
    equations = [line.strip() for line in file if line.strip()]

totalvals = []
elements = []
count = 0
operators = ['+', '*']
total_calibration_result = 0

for eq in equations:
    parts = eq.split(":")
    totalvals.append(int(parts[0])) 
    elements.append([int(x) for x in parts[1].strip().split()]) 

for idx, test_val in enumerate(totalvals):  
    nums = elements[idx]
    n = len(nums) - 1  # Number of operator slots
    found = False

    for ops in product(operators, repeat=n):
        result = nums[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += nums[i + 1]
            elif op == '*':
                result *= nums[i + 1]

        if result == test_val:
            total_calibration_result += test_val
            found = True
            break  

print(total_calibration_result)

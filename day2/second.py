def is_safe_report(report):
    increasing = True
    decreasing = True
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        if abs(diff) < 1 or abs(diff) > 3:  # Difference must be between 1 and 3
            return False
        
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
    
    return increasing or decreasing

def safe_report_with_one_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True  
    return False  


safe_reports = 0

with open("input.txt") as file:
    for line in file:
        report = list(map(int, line.split()))

        if is_safe_report(report):
            safe_reports += 1
        elif safe_report_with_one_removal(report):
            safe_reports += 1

print(safe_reports)



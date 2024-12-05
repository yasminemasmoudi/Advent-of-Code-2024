
with open("input.txt") as file:
    both_sections = file.read().strip().split("\n\n")

    ordering_rules = both_sections[0].splitlines()
    list_of_updates = both_sections[1].splitlines()

    rules = []
    for rule in ordering_rules:
        x, y = map(int, rule.split('|'))  
        rules.append((x, y))            

    updates = []
    for update in list_of_updates:
        updates.append([int(page) for page in update.split(',')])

def is_update_valid(update, rules):
    # Create a dictionary to store the position of each page in the update
    position = {}
    for i in range(len(update)):
        position[update[i]] = i 
    
    # Check each rule
    for x, y in rules:
        if x in position and y in position:
            if position[x] >= position[y]:
                return False
    return True

middle_sum = 0
for update in updates:
    if is_update_valid(update, rules):
        middle_sum += update[len(update) // 2] 


print(middle_sum)

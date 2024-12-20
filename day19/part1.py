with open('input.txt', "r") as file:
    both_sections = file.read().strip().split("\n\n")

    patterns = both_sections[0].split(", ") 
    designs = both_sections[1].splitlines()

def can_create_design(design, patterns):
    if design == "":
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if can_create_design(design[len(pattern):], patterns):
                return True
    return False


count = 0
for design in designs:
    if can_create_design(design, patterns):
        count += 1 

print (count)

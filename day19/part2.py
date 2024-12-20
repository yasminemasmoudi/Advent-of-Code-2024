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


def number_ways(design, patterns, cache):
    if design == "":
        return 1
    if design in cache:
        return cache[design]
    
    ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            ways += number_ways(design[len(pattern):],patterns,cache)
    
    cache[design] = ways
    return ways

count = 0
cache = {}
for design in designs:
    count += number_ways(design,patterns,cache)

print (count)

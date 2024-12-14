from functools import cache

def get_current_stones(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_len = len(str(stone))
        return [int(stone_str[:stone_len//2]),int(stone_str[stone_len//2:])]
    return [stone * 2024]


def part1():
    with open("input.txt", "r") as file:
        line = file.readline().strip()
        
    stones = list(map(int, line.split(" ")))
    
    for i in range(25):
        temp_stones = []
        for stone in stones:
            temp_stones.extend(get_current_stones(stone))
        stones = temp_stones
    return len(stones)

#MEMOIZATION
@cache
def count_stones(stone, blink):
    if blink == 0:
        return 1
    total_stones = 0
    for current_stone in get_current_stones(stone):
        total_stones += count_stones(current_stone, blink-1)
    return total_stones

def part2():
    with open("input.txt", "r") as file:
        line = file.readline().strip()
        
    stones = list(map(int, line.split(" ")))
    tot = 0
    for stone in stones:
        tot+=count_stones(stone, 75)
        
    return tot

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
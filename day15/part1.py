import os

def read_input(input_file):
    with open(input_file, "r") as file:
        input = file.read().split('\n\n')

    grid = input[0].split('\n')
    directions = [ARROWS_TO_DIRECTION[arrow] for arrow in input[1].replace('\n', '')]

    pos = find_in_grid(grid, '@')
    assert len(pos) == 1, f"Multiple start positions found: {pos}"

    return grid, pos[0], directions

DIRECTIONS = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
ARROWS_TO_DIRECTION = {'^': DIRECTIONS['^'], '>': DIRECTIONS['>'], 'v': DIRECTIONS['v'], '<': DIRECTIONS['<']}

def find_in_grid(grid, entity):
    positions = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == entity:
                positions.append((x, y))
    return positions

def add_pos(pos1, pos2):
    return tuple(p1 + p2 for p1, p2 in zip(pos1, pos2))

def tile(grid, pos):
    x, y = pos
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        return grid[y][x]
    return '#'

def update_grid_row(grid, pos, value):
    row = grid[pos[1]]
    grid[pos[1]] = row[:pos[0]] + value + row[pos[0] + 1:]

def update_grid(grid, from_pos, to_pos, value):
    update_grid_row(grid, from_pos, '.')
    update_grid_row(grid, to_pos, value)

def move(grid, from_pos, direction, obj):
    to_pos = add_pos(from_pos, direction)
    if tile(grid, to_pos) == '#':
        return from_pos

    if tile(grid, to_pos) == 'O':
        move(grid, to_pos, direction, 'O')

    if tile(grid, to_pos) == '.':
        update_grid(grid, from_pos, to_pos, obj)
        return to_pos

    return from_pos

def checksum(grid):
    result = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O':
                result += (y * 100) + x
    return result

def solve(input_file):
    grid, pos, directions = read_input(input_file)
    for direction in directions:
        pos = move(grid, pos, direction, '@')
    return checksum(grid)

def main():
    input_file = "input.txt"
    result = solve(input_file)
    print(f"Part 1 Result: {result}")

if __name__ == "__main__":
    main()

# Part 2: Count X-MAS patterns

def count_x_mas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def matches_mas(sequence):
        return sequence in ("MAS", "SAM")

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            top_left_diag = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            top_right_diag = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]

            if matches_mas(top_left_diag) and matches_mas(top_right_diag):
                count += 1

    return count

with open('input.txt') as file:
    grid = [list(line.strip()) for line in file if line.strip()]
    x_mas_count = count_x_mas_patterns(grid)
    print(x_mas_count)
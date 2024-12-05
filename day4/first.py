
word="XMAS"

with open("input.txt") as file:
    grid = [line.strip() for line in file if line.strip()]
    
rows, cols = len(grid), len(grid[0])
all_lines = []
all_lines.extend(grid)

# Collect all columns
for col in range(cols):
    all_lines.append("".join(grid[row][col] for row in range(rows)))

# Collect all diagonals (top-left to bottom-right)
for d in range(-rows + 1, cols):
    all_lines.append("".join(grid[r][c] for r in range(rows) for c in range(cols) if r - c == d))

# Collect all diagonals (top-right to bottom-left)
for d in range(rows + cols - 1):
    all_lines.append("".join(grid[r][c] for r in range(rows) for c in range(cols) if r + c == d))

# Count occurrences of "XMAS" and "SAMX" (reverse of "XMAS") in all lines
count = 0
for line in all_lines:
    count += line.count(word)
    count += line.count(word[::-1])

print(count)

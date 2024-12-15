import numpy as np
from collections import deque

def part1():
    with open("input.txt") as file:
        matrix = [list(line.strip()) for line in file if line.strip()]
        
    rows, columns = len(matrix), len(matrix[0])

    directions = [(-1, 0),(0, 1),(1, 0), (0, -1)]  
    visited = np.zeros((rows, columns), dtype=bool)
    total_price = 0

    def bfs(start, plant_type):
        queue = deque([start])
        visited[start] = True
        area = 0
        perimeter = 0


        while queue:
            x, y = queue.popleft()
            area +=1


            # Check all four directions
            for dx, dy in directions:
                nx,ny = x+dx , y+dy
                if not (0 <= nx < rows and 0 <= ny < columns) or matrix[nx][ny] != plant_type:
                    perimeter += 1
                elif not visited[nx, ny]:
                    visited[nx, ny] = True
                    queue.append((nx, ny))
        return area, perimeter
    
    for i in range(rows):
        for j in range(columns):
            if not visited[i, j]:
                plant_type = matrix[i][j]
                area, perimeter = bfs((i, j), plant_type)
                total_price += area * perimeter

    return total_price

def part2():
    with open("input.txt") as file:
        matrix = [list(line.strip()) for line in file if line.strip()]
        
    rows, columns = len(matrix), len(matrix[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = np.zeros((rows, columns), dtype=bool)
    total_price = 0

    def sides_bfs(start, plant_type):
        queue = deque([start])
        visited[start] = True
        area = 0
        sides = 0

        while queue:
            x, y = queue.popleft()
            area += 1

            for d, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < rows and 0 <= ny < columns) or matrix[nx][ny] != plant_type:
                    newR_90CC = x + directions[(d - 1) % 4][0]
                    newC_90CC = y + directions[(d - 1) % 4][1]
                    isBeginEdge = not (0 <= newR_90CC < rows and 0 <= newC_90CC < columns) or matrix[newR_90CC][newC_90CC] != plant_type
                    newR_Corner = nx + directions[(d - 1) % 4][0]
                    newC_Corner = ny + directions[(d - 1) % 4][1]
                    isConcaveBeginEdge = (
                        0 <= newR_Corner < rows
                        and 0 <= newC_Corner < columns
                        and matrix[newR_Corner][newC_Corner] == plant_type
                    )
                    if isBeginEdge or isConcaveBeginEdge:
                        sides += 1
                elif not visited[nx, ny]:
                    visited[nx, ny] = True
                    queue.append((nx, ny))
        return area, sides
    
    for i in range(rows):
        for j in range(columns):
            if not visited[i, j]:
                plant_type = matrix[i][j]
                area, sides = sides_bfs((i, j), plant_type)
                total_price += area * sides

    return total_price

    

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
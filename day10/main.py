from collections import deque

def is_valid_move(x, y, height, visited):
    return 0 <= x < len(height) and 0 <= y < len(height[0]) and not visited[x][y]

def bfs(start, height): #BFS (Breadth-First Search) starting from each trailhead (height = 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up down left right
    queue = deque([start])
    visited = [[False] * len(height[0]) for _ in range(len(height))]
    visited[start[0]][start[1]] = True
    count_9 = 0
    
    while queue:
        x, y = queue.popleft()
        
        if height[x][y] == 9:
            count_9 += 1
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, height, visited) and height[nx][ny] == height[x][y] + 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return count_9
    
def part1():
    with open("input.txt", 'r') as f:
        height = [list(map(int, line.strip())) for line in f.readlines()]
        #print(height)
        trailhead_scores = 0

        for i in range(len(height)): #rows
            for j in range(len(height[0])): #columns
                if height[i][j] == 0:  # Found a trailhead
                    trailhead_scores += bfs((i, j), height) 
    return trailhead_scores

print(part1()) 

def bfs_part2(start, height):
    """Find the number of distinct hiking trails in Part 2."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [])])  # Each element is (current_position, trail_path)
    trail_paths = set()  # To store distinct trails as tuples

    while queue:
        (x, y), path = queue.popleft()
        path = path + [(x, y)]

        if height[x][y] == 9:
            # Add the path as a tuple to ensure uniqueness
            trail_paths.add(tuple(path))
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(height) and 0 <= ny < len(height[0]) and height[nx][ny] == height[x][y] + 1:
                queue.append(((nx, ny), path))

    return len(trail_paths)

def part2():
    with open("input.txt", 'r') as f:
        height = [list(map(int, line.strip())) for line in f.readlines()]
        total_rating = 0
        for i in range(len(height)):
            for j in range(len(height[0])):
                if height[i][j] == 0:  # Found a trailhead
                    total_rating += bfs_part2((i, j), height)
    return total_rating


print(part2())


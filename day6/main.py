import numpy as np


def part1():
    # Read the file and strip newline characters
    matrix = []
    count = 1
    with open("input.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
        for line in lines:
            matrix.append(list(char for char in line))
        
    arr =  np.array(matrix)
    rows, columns = arr.shape


    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    current_direction = ''
    current_position = (0, 0)

    for i in range(rows):
        for j in range(columns):
            if arr[i,j] in directions:
                current_position = (i,j)
                current_direction = arr[i,j]
                break
        if current_direction:
            break
                
    visited_positions = set()
    visited_positions.add(current_position)

    while True:
        i, j = current_position
        di, dj = directions[current_direction]
        next_position = (i+di, j+dj)

        # Check if the next position is within bounds
        if (0 <= next_position[0] < rows) and (0 <= next_position[1] < columns):
            if arr[next_position] == '#':  # Obstacle ahead
                current_direction = turn_right[current_direction]
            else: 
                current_position = next_position
                visited_positions.add(current_position)
        
        else:
            break
    print (len(visited_positions))

#part1()

def part2():
        # Read the file and strip newline characters
    matrix = []
    count = 1
    with open("input.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
        for line in lines:
            matrix.append(list(char for char in line))
        
    arr =  np.array(matrix)
    rows, columns = arr.shape


    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    current_direction = ''
    current_position = (0, 0)

    for i in range(rows):
        for j in range(columns):
            if arr[i,j] in directions:
                current_position = (i,j)
                current_direction = arr[i,j]
                break
        if current_direction:
            break

    
    obstruction_positions = set()
    for i in range(rows):
        for j in range(columns):
            if (i, j) == current_position or arr[i, j] == '#':
                continue
        
                
            test_arr = arr.copy()
            test_arr[i,j] = '#'
            test_position = current_position
            test_direction = current_direction
            test_path = set()
            test_path.add((test_position, test_direction))

            while True:
                ti, tj = test_position
                tdi, tdj = directions[test_direction]
                next_test_position = (ti + tdi, tj + tdj)

                if 0 <= next_test_position[0] < rows and 0 <= next_test_position[1] < columns:
                    if test_arr[next_test_position] == '#':  
                        test_direction = turn_right[test_direction]
                    else: 
                        test_position = next_test_position
                        if (test_position, test_direction) in test_path:
                            obstruction_positions.add((i, j))
                            break
                        test_path.add((test_position, test_direction))
                else:  
                    break

    print(len(obstruction_positions))        


part2()



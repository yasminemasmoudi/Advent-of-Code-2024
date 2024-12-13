def parse_disk_map(disk_map):
    """
    Parse the disk map to create a list of blocks (file IDs and free spaces).
    """
    blocks = []
    file_id = 0
    is_file = True
    for length in disk_map:
        length = int(length)
        if is_file:
            blocks.extend([file_id] * length)  # Add file blocks
            file_id += 1
        else:
            blocks.extend(['.'] * length)  # Add free spaces
        is_file = not is_file  # Alternate between file and free space
    return blocks

def compact_disk(blocks):
    """
    Simulate the compaction of the disk where file blocks move to the leftmost free spaces.
    """
    steps = []  # To store all intermediate states
    while True:
        moved = False
        # Loop through the blocks to find file blocks and move them
        for i in range(len(blocks)):
            if blocks[i] != '.':  # If it's a file block
                for j in range(i):
                    if blocks[j] == '.':  # Find the first free space
                        # Move the file block to the free space
                        blocks[j], blocks[i] = blocks[i], blocks[j]
                        moved = True
                        # Log the state after the move
                        steps.append(''.join(str(x) if x != '.' else '.' for x in blocks))
                        break  # Move to the next file block
        if not moved:  # If no block moved, compaction is complete
            break
    return steps

def calculate_checksum(blocks):
    """
    Calculate the checksum as the sum of position * file ID for each file block.
    """
    checksum = 0
    for position, block in enumerate(blocks):
        if block != '.':  # Only consider file blocks
            checksum += position * block
    return checksum

def solve_puzzle(disk_map):
    """
    Solve the disk compacting puzzle.
    """
    blocks = parse_disk_map(disk_map)
    steps = compact_disk(blocks)
    checksum = calculate_checksum(blocks)
    return steps, checksum

# Example Input
example_input = "2333133121414131402"
steps, result = solve_puzzle(example_input)

# Print out the steps to show the compaction process
for step in steps:
    print(step)

print(f"The resulting checksum for the example input is: {result}")

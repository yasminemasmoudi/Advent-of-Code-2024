def part1():
    with open("input.txt", "r") as file:
        line = file.readline().strip()

    blocks = []
    file_id = 0

    for i in range(len(line)):
        length = int(line[i])
        if i % 2 == 0:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(['.'] * length)

    # Pointers for compacting the blocks
    start = 0
    end = len(blocks) - 1

    while start < end:
        if blocks[start] == '.':
            if blocks[end] != '.':
                # Swap non-free block from the end to the start
                blocks[start], blocks[end] = blocks[end], '.'
                start += 1
                end -= 1
            else:
                end -= 1
        else:
            start += 1

    checksum = 0
    for position, block in enumerate(blocks):
        if block != '.':
            checksum += position * block

    return checksum

def part2():
    with open("input.txt", "r") as file:
        line = file.readline().strip()

    blocks = []
    file_lengths = []
    file_id = 0

    i = 0
    while i < len(line):
        length = int(line[i])
        if i % 2 == 0:
            file_lengths.append(length)
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(['.'] * length)
        i += 1

    file_list = list(enumerate(file_lengths))
    file_list.sort(key=lambda x: x[0], reverse=True)

    for file_id, file_length in file_list:
        start_index = blocks.index(file_id)
        
        free_start = 0
        while free_start < start_index:
            free_count = 0
            j = free_start
            while j < start_index and blocks[j] == '.':
                free_count += 1
                j += 1
            
            if free_count >= file_length:
                for k in range(start_index, start_index + file_length):
                    blocks[k] = '.'
                
                for k in range(free_start, free_start + file_length):
                    blocks[k] = file_id
                break
            
            free_start += 1

    checksum = 0
    for position, block in enumerate(blocks):
        if block != '.':
            checksum += position * block

    return checksum

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
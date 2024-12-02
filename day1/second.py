def second():
    lines = []

    # Read the file and strip newline characters
    with open("input.txt") as file:
        lines = file.readlines()

    location_list = []
    freq_map = {}

    for i in range(len(lines)):
        location_list.append(int(lines[i].split(' ')[0]))
        freq_key = int(lines[i].split(' ')[-1])
        freq_map[freq_key] = freq_map.get(freq_key,0) + 1

    similarity_score = 0

    for i in range(len(location_list)):
        if freq_map.get(location_list[i], 0) != 0:
            similarity_score += location_list[i] * freq_map[location_list[i]]

    print(similarity_score)

second()
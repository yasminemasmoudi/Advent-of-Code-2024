# Parse the input as before
with open("input.txt") as file:
    ordering_rules, list_of_updates = file.read().strip().split("\n\n")

    rules = []
    for rule in ordering_rules.splitlines():
        x, y = rule.split('|')
        rules.append((int(x), int(y)))

    updates = []
    for update in list_of_updates.splitlines():
        updates.append([int(page) for page in update.split(',')])

    def is_update_valid(update, rules):
        position = {page: i for i, page in enumerate(update)}
        for x, y in rules:
            if x in position and y in position:
                if position[x] >= position[y]:  
                    return False
        return True

    def sort_update(update, rules):
        graph = {page: [] for page in update}
        in_degree = {page: 0 for page in update}

        for x, y in rules:
            if x in graph and y in graph:
                graph[x].append(y)
                in_degree[y] += 1

        queue = [page for page in update if in_degree[page] == 0]
        sorted_update = []

        while queue:
            page = queue.pop(0)  
            sorted_update.append(page)

            for neighbor in graph[page]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  

        return sorted_update

    middle_sum = 0
    for update in updates:
        if not is_update_valid(update, rules):  # If the update is not in the correct order
            sorted_update = sort_update(update, rules)
            middle_sum += sorted_update[len(sorted_update) // 2]  # Add the middle page number

    print(middle_sum)

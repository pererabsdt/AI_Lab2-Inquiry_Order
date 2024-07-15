from collections import deque


def read_input_file(input_file):
    adjacency_list = {}
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(": ")
            key = key.strip("'")
            value = value.strip('[],').replace("'", "").split(", ")
            if value == ['']:
                value = []

            adjacency_list[key] = value

    return adjacency_list


def bfs(adjacency_list, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if not node in visited:
            visited.append(node)
            neighbours = adjacency_list.get(node, [])
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)

    return visited


input_file = 'input.txt'
inquiry_tree = read_input_file(input_file)
root_inquiry = 'root'
process_order = bfs(inquiry_tree, root_inquiry)
print(process_order)

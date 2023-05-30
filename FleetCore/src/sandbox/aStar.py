def astar(start, end, heuristic_cost, get_reachable_nodes):
    open_set = [(0, start)]  # List for open set
    g_scores = {start: 0}  # Dictionary for g scores
    parent_map = {start: None}  # Dictionary to store parent nodes

    while open_set:
        current = min(open_set, key=lambda node: node[0] + heuristic_cost(node[1], end))

        if current[1] == end:
            return reconstruct_path(parent_map, end)

        open_set = [node for node in open_set if node[1] != current[1]]

        for neighbor, distance in get_reachable_nodes(current[1]):
            new_g = g_scores[current[1]] + distance

            if neighbor not in g_scores or new_g < g_scores[neighbor]:
                g_scores[neighbor] = new_g
                parent_map[neighbor] = current[1]

                # f = g + h (total cost)
                f = new_g + heuristic_cost(neighbor, end)
                open_set.append((f, neighbor))

    return None  # No path found


def reconstruct_path(parent_map, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent_map[current]

    return list(reversed(path))


# Example usage:

# Dictionary to store reachable nodes from each node
reachable_nodes = {
    'Start': [('Node 1', 4), ('Node 2', 2)],
    'Node 1': [('Node 2', 1), ('Node 3', 5)],
    'Node 2': [('Node 3', 2), ('End', 3)],
    'Node 3': [('End', 1)],
    'End': []
}

# Heuristic function (manhattan distance between nodes)
def heuristic_cost(node, end):
    return abs(ord(node[0]) - ord(end[0]))

# Running A* algorithm
path = astar('Start', 'End', heuristic_cost, reachable_nodes.get)

if path:
    print("Shortest path:", path)
else:
    print("No path found.")

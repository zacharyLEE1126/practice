import numpy as np

map_grid = [[np.inf for i in range(0, 10)] for j in range(0, 10)]
for i in range(0, 10):
    map_grid[i][i] = 0  # set node distance between itself as 0

map_grid[0][1] = 1.2
map_grid[0][2] = 2.3
map_grid[1][5] = 7.5
map_grid[1][3] = 5.6
map_grid[1][4] = 1.7
map_grid[2][3] = 1.9
map_grid[2][4] = 2.6
map_grid[5][6] = 1.6
map_grid[3][6] = 2.6
map_grid[4][6] = 3.6
map_grid[4][7] = 1.7
map_grid[4][8] = 3.6
map_grid[6][9] = 1.9
map_grid[7][9] = 1.7
map_grid[8][9] = 3.6

map_grid = np.array(map_grid)
np.savetxt("map_grid.txt", map_grid)


def all_possible_path(start_node, end_node, graph):
    return get_all_possible_path(end_node, [start_node], graph, list())  # DFS recursive


def get_all_possible_path(end_node, current_path, graph, output_path):
    last_node = current_path[-1]
    if last_node == end_node:
        output_path.append(list(current_path))
    else:
        for neighbor in range(0, 10):
            if 0 < graph[last_node][neighbor] < 1000:  # for each weight far less than 1000
                current_path.append(neighbor)
                get_all_possible_path(end_node, current_path, graph, output_path)
                current_path.pop()
    # print(output_path)
    return output_path


def dijkstra(start_node, end_node, graph):
    unvisited_node = list(range(0, 10))
    shortest_path = {}
    output_path = list()
    previous_node = 0
    for node in unvisited_node:
        shortest_path[node] = np.inf
    shortest_path[start_node] = 0
    while end_node in unvisited_node:
        temp_min_node = None
        for node in unvisited_node:
            if temp_min_node is None:
                temp_min_node = node
            elif shortest_path[node] < shortest_path[temp_min_node]:
                temp_min_node = node
        if temp_min_node == end_node:
            break
        temp_shortest_cost = np.inf
        for neighbor in range(0, 10):
            if 0 < graph[temp_min_node][neighbor] < 1000:
                temp_cost = shortest_path[temp_min_node] + graph[temp_min_node][neighbor]
                if temp_cost < temp_shortest_cost:
                    temp_shortest_cost = temp_cost
                    shortest_path[neighbor] = temp_shortest_cost
                    previous_node = temp_min_node
        output_path.append(previous_node)
        unvisited_node.remove(temp_min_node)
    output_path.append(int(end_node))
    return output_path, shortest_path[end_node]


filename = "map_grid.txt"
graph_grid = np.loadtxt(filename)
# get_num_paths(filename)
path_num = len(all_possible_path(0, 9, graph_grid))
print("Total possible paths number is", path_num)

[shortest_path_way, min_cost] = dijkstra(0, 9, graph_grid)
print("The shortest path to destination is", shortest_path_way, "with minimum cost", min_cost)

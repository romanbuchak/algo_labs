from graph import Graph, INT_MAX


def get_min_latency(graph: Graph, clients: list) -> int:
    min_path_length = INT_MAX

    for current_node in range(1, len(graph.nodes) + 1):
        if current_node not in clients:
            max_path_length = 0
            paths_to_all_nodes = graph.dijkstra(current_node)

            for client_node in clients:
                if max_path_length < paths_to_all_nodes[client_node]:
                    max_path_length = paths_to_all_nodes[client_node]

            if min_path_length > max_path_length:
                min_path_length = max_path_length
    return min_path_length


def main(IN_FILE='gamsrv.in', OUT_FILE='gamsrv.out') -> None:
    graph = Graph()
    with open(IN_FILE, 'r') as in_file:
        file_data = in_file.readlines()

    clients = list(map(int, file_data[1].split(' ')))
    edges = file_data[2:]

    for edge in edges:
        start_node, end_node, latency = list(map(int, edge.split(' ')))
        graph.add_two_sided_edge(start_node, end_node, latency)

    min_path_length = get_min_latency(graph, clients)

    open(OUT_FILE, 'w').write(str(min_path_length))


if __name__ == '__main__':
    main()
import networkx as nx


def compute_degree_centrality(graph, normalized=True):
    """
    Computes the degree centrality for each node in the given graph.

    Parameters:
    graph (networkx.Graph): The input graph.

    Returns:
    dict: A dictionary with nodes as keys and their degree centrality as values.
    """
    node_degree_centrality = {}
    for node in graph.nodes():
        # Normalize by dividing by (N-1) where N is the number of nodes in the graph
        degree_centrality = graph.degree(node)
        if normalized:
            node_degree_centrality[node] = degree_centrality / (len(graph.nodes()) - 1)
        else:
            node_degree_centrality[node] = degree_centrality
    return node_degree_centrality

def compute_betweenness_centrality(graph, normalized=True):

    node_betweenness_centrality = {}
    for node in graph.nodes():
        node_betweenness_centrality[node] = 0
    # Precompute all pairs shortest paths
    all_shortest_paths = dict(nx.all_pairs_shortest_path(graph))
    # Go over nodes in the shortest paths and count occurrences not including itself to itself
    for path in all_shortest_paths.values():
        for source_node, target_paths in path.items():
            for target_node, shortest_path in target_paths.items():
                if source_node != target_node:
                    for intermediate_node in shortest_path[1:-1]:
                        node_betweenness_centrality[intermediate_node] += 1
    # Normalize the betweenness centrality values
    if normalized:
        scale = 1 / ((len(graph.nodes()) - 1) * (len(graph.nodes()) - 2))
        for node in node_betweenness_centrality:
            node_betweenness_centrality[node] *= scale
    return node_betweenness_centrality

def compute_closeness_centrality(graph, normalized=True):
    """
    computes the closeness centrality for each node in the given graph.
    Parameters:
    graph (networkx.Graph): The input graph.

    Returns: A dictionary with nodes as keys and their closeness centrality as values.

    """
    node_closeness_centrality = {}
    for node in graph.nodes():
        path_length_sum = 0
        for target_node in graph.nodes():
            if node != target_node:
                try:
                    path_length = nx.shortest_path_length(graph, source=node, target=target_node)
                    path_length_sum += path_length
                except nx.NetworkXNoPath:
                    # If there is no path, we can consider the distance as infinite
                    path_length_sum += float('inf')
            if path_length_sum > 0 and path_length_sum != float('inf'):
                if normalized:
                    closeness_centrality = (len(graph.nodes()) - 1) / path_length_sum
                else:
                    closeness_centrality = 1 / path_length_sum
                node_closeness_centrality[node] = closeness_centrality
    return node_closeness_centrality

import networkx as nx
import random

def watts_strogatz_model(n, k, p):
    """
    Implement the Watts-Strogatz small-world model.
    
    Parameters:
    -----------
    n : int
        Number of nodes
    k : int
        Each node is connected to k nearest neighbors in ring topology
        (k/2 on each side). Must be even and k < n.
    p : float
        Probability of rewiring each edge (0 <= p <= 1)
    
    Returns:
    --------
    G : networkx.Graph
        Watts-Strogatz small-world graph
    
    Raises:
    -------
    ValueError
        If k is odd, k >= n, or p is not in [0, 1]
    
    Examples:
    ---------
    >>> G = watts_strogatz_model(20, 4, 0.3)
    >>> print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    """
    # Input validation
    if k % 2 != 0:
        raise ValueError("k must be even")
    if k >= n:
        raise ValueError("k must be less than n")
    if not 0 <= p <= 1:
        raise ValueError("p must be between 0 and 1")
    
    # Step 1: Create ring lattice
    G = nx.Graph()
    nodes = list(range(n))
    G.add_nodes_from(nodes)
    
    # Connect each node to k/2 neighbors on the right
    for i in range(n):
        for j in range(1, k // 2 + 1):
            target = (i + j) % n
            G.add_edge(i, target)
    
    # Step 2: Rewire edges with probability p
    # Only consider edges where i < j to avoid processing each edge twice
    edges_to_process = [(i, j) for i, j in G.edges() if i < j]
    
    for i, j in edges_to_process:
        if random.random() < p:
            # Find valid targets (not i, not already connected to i)
            valid_targets = [node for node in nodes 
                           if node != i and not G.has_edge(i, node)]
            
            # Only rewire if there are valid targets
            if valid_targets:
                new_target = random.choice(valid_targets)
                G.remove_edge(i, j)
                G.add_edge(i, new_target)
    
    return G


# Test the implementation
if __name__ == "__main__":
    print("Testing Watts-Strogatz Model Implementation")
    print("=" * 50)
    
    # Test 1: Regular ring lattice (p=0)
    print("\nTest 1: Regular ring lattice (p=0)")
    G1 = watts_strogatz_model(10, 4, 0)
    print(f"Nodes: {G1.number_of_nodes()}, Edges: {G1.number_of_edges()}")
    print(f"Expected edges: {10 * 4 // 2} (n * k / 2)")
    degrees1 = [d for _, d in G1.degree()]
    print(f"All degrees equal to k? {all(d == 4 for d in degrees1)}")
    
    # Test 2: Small-world network (p=0.3)
    print("\nTest 2: Small-world network (p=0.3)")
    G2 = watts_strogatz_model(20, 6, 0.3)
    print(f"Nodes: {G2.number_of_nodes()}, Edges: {G2.number_of_edges()}")
    degrees2 = [d for _, d in G2.degree()]
    print(f"Degree range: min={min(degrees2)}, max={max(degrees2)}, avg={sum(degrees2)/len(degrees2):.2f}")
    
    # Test 3: Fully rewired (p=1.0)
    print("\nTest 3: Fully rewired network (p=1.0)")
    G3 = watts_strogatz_model(20, 4, 1.0)
    print(f"Nodes: {G3.number_of_nodes()}, Edges: {G3.number_of_edges()}")
    degrees3 = [d for _, d in G3.degree()]
    print(f"Degree range: min={min(degrees3)}, max={max(degrees3)}, avg={sum(degrees3)/len(degrees3):.2f}")
    
    # Test 4: Error handling
    print("\nTest 4: Input validation")
    try:
        G4 = watts_strogatz_model(10, 5, 0.3)  # k must be even
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
    
    try:
        G5 = watts_strogatz_model(10, 10, 0.3)  # k must be < n
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
    
    try:
        G6 = watts_strogatz_model(10, 4, 1.5)  # p must be in [0, 1]
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")

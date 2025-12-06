import networkx as nx
import matplotlib.pyplot as plt

# Import the centrality functions from q2
from q2 import compute_degree_centrality, compute_betweenness_centrality, compute_closeness_centrality

# Create the same Erdos-Renyi graph
n = 22
p = 0.3
G = nx.erdos_renyi_graph(n, p, seed=42)

# Compute centrality measures
degree_centrality = compute_degree_centrality(G)
betweenness_centrality = compute_betweenness_centrality(G)
closeness_centrality = compute_closeness_centrality(G)

# Create figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Get the layout once for consistency across all plots
pos = nx.spring_layout(G, seed=42)

# Scale factor for node sizes (multiply by a constant to make them visible)
scale_factor = 3000

# Plot 1: Degree Centrality
node_sizes_degree = [degree_centrality[node] * scale_factor for node in G.nodes()]
nx.draw(G, pos, ax=axes[0], node_size=node_sizes_degree, node_color='lightblue', 
        with_labels=True, font_size=10, font_weight='bold', edge_color='gray')
axes[0].set_title('Network by Degree Centrality', fontsize=14, fontweight='bold')

# Plot 2: Betweenness Centrality
node_sizes_betweenness = [betweenness_centrality[node] * scale_factor for node in G.nodes()]
nx.draw(G, pos, ax=axes[1], node_size=node_sizes_betweenness, node_color='lightgreen',
        with_labels=True, font_size=10, font_weight='bold', edge_color='gray')
axes[1].set_title('Network by Betweenness Centrality', fontsize=14, fontweight='bold')

# Plot 3: Closeness Centrality
node_sizes_closeness = [closeness_centrality[node] * scale_factor for node in G.nodes()]
nx.draw(G, pos, ax=axes[2], node_size=node_sizes_closeness, node_color='lightcoral',
        with_labels=True, font_size=10, font_weight='bold', edge_color='gray')
axes[2].set_title('Network by Closeness Centrality', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('q2c_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nVisualization complete! The plot has been saved as 'q2c_visualization.png'")
print("\nNode sizes are proportional to their centrality values:")
print("- Larger nodes = higher centrality")
print("- Smaller nodes = lower centrality")

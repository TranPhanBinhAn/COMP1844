import matplotlib.pyplot as plt
import networkx as nx

# Create graph
G = nx.Graph()

# --- Add edges with real distances and correct line colours ---

# Bakerloo Line (brown-orange)
G.add_edge("Oxford Circus", "Piccadilly Circus", weight=0.7, color="#B36305")
G.add_edge("Piccadilly Circus", "Charing Cross", weight=0.6, color="#B36305")

# Northern Line (black)
G.add_edge("Charing Cross", "Leicester Square", weight=0.4, color="black")
G.add_edge("Leicester Square", "Piccadilly Circus", weight=0.5, color="black")

# Piccadilly Line (blue)
G.add_edge("Leicester Square", "Covent Garden", weight=0.3, color="blue")

# --- Node positions (match the diagram style) ---
pos = {
    "Oxford Circus": (-1, 2),
    "Piccadilly Circus": (0, 1),
    "Charing Cross": (0, -0.2),
    "Leicester Square": (1.2, 0.7),
    "Covent Garden": (2.3, 1.0)
}

# Extract edge colours
edge_colors = [G[u][v]["color"] for u, v in G.edges()]

# Plot figure
plt.figure(figsize=(9, 6))

# Draw nodes
nx.draw_networkx_nodes(
    G, pos,
    node_size=700,
    node_color="lightgray",
    edgecolors="black"
)

# Draw edges
nx.draw_networkx_edges(
    G, pos,
    width=3,
    edge_color=edge_colors
)

# Draw station labels
nx.draw_networkx_labels(G, pos, font_size=10)

# Draw edge distance labels
edge_labels = {(u, v): f"{G[u][v]['weight']} km" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# --- Legend / Key ---
plt.text(2.8, 0.6, "Key", fontsize=12, weight="bold")
plt.text(2.8, 0.4, "── Piccadilly", color="blue", fontsize=10)
plt.text(2.8, 0.2, "── Northern", color="black", fontsize=10)
plt.text(2.8, 0.0, "── Bakerloo", color="#B36305", fontsize=10)

plt.axis("off")
plt.tight_layout()
plt.show()

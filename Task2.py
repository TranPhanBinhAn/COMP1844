import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# ============================
# ADD ALL LINES + DISTANCES
# ============================

# --- Piccadilly Line (blue) ---
G.add_edge("Holborn", "Covent Garden", weight=0.5, color="blue")
G.add_edge("Covent Garden", "Leicester Square", weight=0.3, color="blue")
G.add_edge("Leicester Square", "Piccadilly Circus", weight=0.5, color="blue")
G.add_edge("Piccadilly Circus", "Green Park", weight=0.6, color="blue")
G.add_edge("Green Park", "Hyde Park Corner", weight=0.8, color="blue")

# --- Bakerloo Line (brown) ---
G.add_edge("Marylebone", "Baker Street", weight=0.4, color="#B36305")
G.add_edge("Baker Street", "Regent's Park", weight=0.7, color="#B36305")
G.add_edge("Regent's Park", "Oxford Circus", weight=1.0, color="#B36305")
G.add_edge("Oxford Circus", "Piccadilly Circus", weight=0.7, color="#B36305")
G.add_edge("Piccadilly Circus", "Charing Cross", weight=0.6, color="#B36305")

# --- Northern Line (black) ---
G.add_edge("Euston", "Warren Street", weight=0.5, color="black")
G.add_edge("Warren Street", "Goodge Street", weight=0.5, color="black")
G.add_edge("Goodge Street", "Tottenham Court Road", weight=0.6, color="black")
G.add_edge("Tottenham Court Road", "Leicester Square", weight=0.5, color="black")
G.add_edge("Leicester Square", "Charing Cross", weight=0.3, color="black")

# --- Central Line (red) ---
G.add_edge("Notting Hill Gate", "Queensway", weight=0.6, color="red")
G.add_edge("Queensway", "Marble Arch", weight=2.0, color="red")
G.add_edge("Marble Arch", "Bond Street", weight=0.6, color="red")
G.add_edge("Bond Street", "Oxford Circus", weight=0.5, color="red")
G.add_edge("Oxford Circus", "Tottenham Court Road", weight=0.8, color="red")

# ============================
# NODE POSITIONS — MATCH TASK 1 CENTER
# ============================

pos = {
    "Oxford Circus": (-1, 2),
    "Piccadilly Circus": (0, 1),
    "Charing Cross": (0, -0.2),
    "Leicester Square": (1.2, 0.7),
    "Covent Garden": (2.3, 1.0),

    "Holborn": (3.3, 1.0),
    "Green Park": (-1.2, 1.0),
    "Hyde Park Corner": (-2.2, 1.0),

    "Regent's Park": (-2, 3.5),
    "Baker Street": (-3, 3.5),
    "Marylebone": (-4, 3.5),

    "Tottenham Court Road": (1.2, 2.2),
    "Goodge Street": (1.2, 3.2),
    "Warren Street": (1.2, 4.2),
    "Euston": (1.2, 5.2),

    "Notting Hill Gate": (-4, -1),
    "Queensway": (-3, -1),
    "Marble Arch": (-2, -1),
    "Bond Street": (-1, -1),
}

# ============================
# LABEL OFFSET FOR CLARITY
# ============================

label_offset = {
    "Oxford Circus": (0.2, 0.25),
    "Piccadilly Circus": (0.2, -0.25),
    "Charing Cross": (0.25, -0.25),
    "Leicester Square": (0.25, 0.25),
    "Covent Garden": (0.25, 0.15),

    "Green Park": (-0.25, 0.25),
    "Hyde Park Corner": (-0.25, 0.15),

    "Regent's Park": (-0.25, 0.25),
    "Baker Street": (-0.25, 0.25),
    "Marylebone": (-0.25, 0.25),

    "Tottenham Court Road": (0.25, 0.25),
    "Goodge Street": (0.25, 0.25),
    "Warren Street": (0.25, 0.25),
    "Euston": (0.25, 0.25),

    "Notting Hill Gate": (-0.25, -0.25),
    "Queensway": (-0.25, -0.25),
    "Marble Arch": (-0.25, -0.25),
    "Bond Street": (-0.25, -0.25),
}

# ============================
# DRAWING
# ============================

plt.figure(figsize=(14, 10))

edge_colors = [G[u][v]['color'] for u, v in G.edges()]

# --- NODES WITH GRAY FILL ---
nx.draw_networkx_nodes(
    G, pos, node_size=700,
    node_color="#D3D3D3",   # GRAY FILL
    edgecolors="black"
)

plt.text(3.8, 5.2, "KEY", fontsize=14, weight="bold")

plt.text(3.8, 4.9, "── Piccadilly Line", color="blue", fontsize=10)
plt.text(3.8, 4.6, "── Bakerloo Line", color="#B36305", fontsize=10)
plt.text(3.8, 4.3, "── Northern Line", color="black", fontsize=10)
plt.text(3.8, 4.0, "── Central Line", color="red", fontsize=10)
# EDGES
nx.draw_networkx_edges(G, pos, width=3, edge_color=edge_colors)

for node, (x, y) in pos.items():
    dx, dy = label_offset.get(node, (0, 0))
    plt.text(x + dx, y + dy, node, fontsize=9, ha="center")

edge_labels = {(u, v): f"{G[u][v]['weight']} km" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

plt.axis("off")
plt.tight_layout()
plt.show()

import numpy as np

lengths = [G[u][v]['weight'] for u, v in G.edges()]

total_length = sum(lengths)

average_length = np.mean(lengths)

std_dev = np.std(lengths)

print("=== TASK 3 RESULTS ===")
print(f"Total network length: {total_length:.2f} km")
print(f"Average distance between stations: {average_length:.2f} km")
print(f"Standard deviation: {std_dev:.2f} km")


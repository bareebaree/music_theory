import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def create_db_graph(homology):
    """
    Create a 3D network graph of chord transitions based on note differences.
    Nodes are labeled with chord names, and colored based on chord type.
    """

    # Initialize graph
    G = nx.Graph()

    # Define chord types with their respective names
    chord_types = {
        "Minor": [
            (["A", "C", "E"], "Am"), (["A#", "C#", "F"], "A#m"), (["B", "D", "F"], "Bm"), (["C", "E♭", "G"], "Cm"),
            (["C#", "E", "G#"], "C#m"), (["D", "F", "A"], "Dm"), (["D#", "F#", "A#"], "D#m"), (["E", "G", "B"], "Em"),
            (["F", "G#", "C"], "Fm"), (["F#", "A", "C#"], "F#m"), (["G", "A#", "D"], "Gm"), (["G#", "B", "D#"], "G#m")
        ],
        "Major": [
            (["A", "C#", "E"], "A"), (["A#", "D", "F"], "A#"), (["B", "D#", "F#"], "B"), (["C", "E", "G"], "C"),
            (["C#", "F", "G#"], "C#"), (["D", "F#", "A"], "D"), (["D#", "G", "A#"], "D#"), (["E", "G#", "B"], "E"),
            (["F", "A", "C"], "F"), (["F#", "A#", "C#"], "F#"), (["G", "B", "D"], "G"), (["G#", "C", "D#"], "G#")
        ],
        "Diminished": [
            (["A", "C", "E♭"], "Adim"), (["A#", "C#", "E"], "A#dim"), (["B", "D", "F"], "Bdim"), (["C", "E♭", "G♭"], "Cdim"),
            (["C#", "E", "G"], "C#dim"), (["D", "F", "A♭"], "Ddim"), (["D#", "F#", "A"], "D#dim"), (["E", "G", "B♭"], "Edim"),
            (["F", "G#", "B"], "Fdim"), (["F#", "A", "C"], "F#dim"), (["G", "A#", "C#"], "Gdim"), (["G#", "B", "D"], "G#dim")
        ],
        "Diminished7": [
            (["A", "C", "E♭", "G♭"], "Adim7"), (["A#", "C#", "E", "G"], "A#dim7"), (["B", "D", "F", "A♭"], "Bdim7"),
            (["C", "E♭", "G♭", "B♭"], "Cdim7"), (["C#", "E", "G", "B"], "C#dim7"), (["D", "F", "A♭", "C♭"], "Ddim7"),
            (["D#", "F#", "A", "C"], "D#dim7"), (["E", "G", "B♭", "D♭"], "Edim7"), (["F", "A♭", "B", "D"], "Fdim7"),
            (["F#", "A", "C", "E♭"], "F#dim7"), (["G", "A#", "C#", "E"], "Gdim7"), (["G#", "B", "D", "F"], "G#dim7")
        ],
        "Augmented": [
            (["A", "C#", "E#"], "Aaug"), (["A#", "D", "F#"], "A#aug"), (["B", "D#", "G"], "Baug"), (["C", "E", "G#"], "Caug"),
            (["C#", "F", "A"], "C#aug"), (["D", "F#", "A#"], "Daug"), (["D#", "G", "B"], "D#aug"), (["E", "G#", "B#"], "Eaug"),
            (["F", "A", "C#"], "Faug"), (["F#", "A#", "D"], "F#aug"), (["G", "B", "D#"], "Gaug"), (["G#", "C", "E"], "G#aug")
        ],
        "Minor7": [
            (["A", "C", "E", "G"], "Am7"), (["B", "D", "F#", "A"], "Bm7"), (["C#", "E", "G#", "B"], "C#m7"),
            (["D", "F", "A", "C"], "Dm7"), (["E", "G", "B", "D"], "Em7"), (["F#", "A", "C#", "E"], "F#m7"),
            (["G#", "B", "D#", "F#"], "G#m7"), (["A#", "C#", "E", "G#"], "A#m7"), (["C", "E♭", "G", "B♭"], "Cm7"),
            (["D#", "F#", "A#", "C#"], "D#m7"), (["F", "G#", "C", "D#"], "Fm7"), (["G", "A#", "D", "F"], "Gm7")
        ],
        "MinorMajor7": [
            (["A", "C", "E", "G#"], "AmMaj7"), (["B", "D", "F#", "A#"], "BmMaj7"), (["C#", "E", "G#", "B#"], "C#mMaj7"),
            (["D", "F", "A", "C#"], "DmMaj7"), (["E", "G", "B", "D#"], "EmMaj7"), (["F#", "A", "C#", "E#"], "F#mMaj7"),
            (["G#", "B", "D#", "F##"], "G#mMaj7"), (["A#", "C#", "E", "G#"], "A#mMaj7"), (["C", "E♭", "G", "B"], "CmMaj7"),
            (["D#", "F#", "A#", "C##"], "D#mMaj7"), (["F#", "A", "C#", "E##"], "F#mMaj7"), (["G#", "B", "D#", "F##"], "G#mMaj7")
        ],
        "HalfDiminished": [
            (["A", "C", "E♭", "G"], "Am7♭5"), (["B", "D", "F", "A"], "Bm7♭5"), (["C#", "E", "G", "B"], "C#m7♭5"),
            (["D", "F", "A♭", "C"], "Dm7♭5"), (["E", "G", "B♭", "D"], "Em7♭5"), (["F#", "A", "C", "E"], "F#m7♭5"),
            (["G#", "B", "D", "F#"], "G#m7♭5"), (["A#", "C#", "E", "G#"], "A#m7♭5"), (["C", "E♭", "G♭", "B♭"], "Cm7♭5"),
            (["D#", "F#", "A", "C"], "D#m7♭5"), (["F#", "A", "C", "E♭"], "F#m7♭5"), (["G#", "B", "D", "F"], "G#m7♭5")
        ]
    }


    # Assign colors for each chord type
    color_map = {
        "Minor": "red",
        "Major": "blue",
        "Diminished": "purple",
        "Diminished7": "darkviolet",
        "Augmented": "orange",
        "Minor7": "green",
        "Major7": "yellow",
        "Dominant7": "pink",
        "MinorMajor7": "gold",
        "HalfDiminished": "darkred",
        "Suspended": "cyan"
}
    # Map nodes to chord names and colors
    chord_labels = {}  # Dictionary for node labels
    node_colors = {}   # Dictionary for node colors

    # Add nodes with labels
    for chord_type, chord_list in chord_types.items():
        for chord, name in chord_list:
            chord_tuple = tuple(chord)
            G.add_node(chord_tuple)
            chord_labels[chord_tuple] = name  # Label nodes with chord name
            node_colors[chord_tuple] = color_map[chord_type]

    # Create edges based on homology (shared notes)
    edges = []
    for i in G.nodes:
        for j in G.nodes:
            if i != j and len(set(i) & set(j)) >= homology:
                edges.append((i, j))

    # Add edges to the graph
    G.add_edges_from(edges)

    # Generate 3D node positions
    pos_3d = nx.spring_layout(G, dim=3, seed=42, k = 0.3)  # 3D layout

    # Extract positions into arrays for easy plotting
    x_vals = [pos_3d[n][0] for n in G.nodes]
    y_vals = [pos_3d[n][1] for n in G.nodes]
    z_vals = [pos_3d[n][2] for n in G.nodes]

    # Create 3D figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')


    # Ensure labels appear in front of nodes
    for node, (x, y, z) in zip(G.nodes, zip(x_vals, y_vals, z_vals)):
        ax.scatter(x, y, z, color=node_colors[node], s=100, edgecolor="black", zorder=3)  # Nodes with black edge
        
        # Offset labels slightly in the viewing direction (toward camera)
        label_offset = 0.02  # Adjust this if necessary
        ax.text(x + label_offset, y + label_offset, z + label_offset, 
                chord_labels[node], fontsize=9, ha='center', va='center', zorder=3)

    # Draw edges
    for edge in G.edges:
        x_edge = [pos_3d[edge[0]][0], pos_3d[edge[1]][0]]
        y_edge = [pos_3d[edge[0]][1], pos_3d[edge[1]][1]]
        z_edge = [pos_3d[edge[0]][2], pos_3d[edge[1]][2]]
        ax.plot(x_edge, y_edge, z_edge, color='gray', alpha=0.6)

    # Set labels and title
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"3D Chord Transition Graph (Homology ≥ {homology})")

    plt.show()

    return G

# Run the function with homology threshold of 2
if __name__ == "__main__":
    create_db_graph(homology=2)

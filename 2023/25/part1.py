import networkx as nx

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

wiring = []

for line in data.splitlines():
    component, other = line.split(":")
    connections = other.split()
    for connected in connections:
        wiring.append((component, connected))

G = nx.Graph()

for component, connected in wiring:
    G.add_edge(component, connected)

min_cut = nx.minimum_edge_cut(G)

G.remove_edges_from(min_cut)

group1, group2 = nx.connected_components(G)

print(len(group1) * len(group2))

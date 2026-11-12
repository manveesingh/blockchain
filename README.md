ximport networkx as nx
from collections import defaultdict

# toy transactions: (inputs, outputs, amount)
txs = [
    (["A", "B"], ["X"], 2.0),
    (["B", "C"], ["Y"], 1.5),
    (["D"], ["Z"], 0.7),
    (["E", "D"], ["W"], 3.1),
]

# common-input heuristic: addresses spent together likely share an owner
G = nx.Graph()
for ins, outs, amt in txs:
    G.add_nodes_from(ins + outs)
    for a in ins[1:]:
        G.add_edge(ins[0], a)

clusters = [sorted(c) for c in nx.connected_components(G) if len(c) > 1]
print("Likely same-owner clusters:", clusters)

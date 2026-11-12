import networkx as nx
import matplotlib.pyplot as plt

# toy transactions: (inputs, outputs, amount)
txs = [
    (["A", "B"], ["X"], 2.0),
    (["B", "C"], ["Y"], 1.5),
    (["D"], ["Z"], 0.7),
    (["E", "D"], ["W"], 3.1),
    (["C"], ["P", "Q", "R"], 1.0),   # one address splitting funds many ways
]

# 1. money-flow graph (who paid whom)
flow = nx.DiGraph()
for ins, outs, amt in txs:
    for a in ins:
        for b in outs:
            flow.add_edge(a, b, amount=amt)

# 2. common-input clustering (same-owner guess)
owners = nx.Graph()
owners.add_nodes_from(flow.nodes)
for ins, _, _ in txs:
    for a in ins[1:]:
        owners.add_edge(ins[0], a)
clusters = list(nx.connected_components(owners))

# 3. flag unusual behaviour: high fan-out
flagged = {n for n in flow if flow.out_degree(n) >= 3}

# 4. draw: colour = cluster, red outline = needs attention
palette = ["#4C78A8", "#F58518", "#54A24B", "#B279A2", "#9D9D9D"]
color = {}
for i, c in enumerate(clusters):
    for n in c:
        color[n] = palette[i % len(palette)] if len(c) > 1 else "#D3D3D3"

pos = nx.spring_layout(flow, seed=1)
nx.draw_networkx(
    flow, pos,
    node_color=[color[n] for n in flow],
    edgecolors=["red" if n in flagged else "white" for n in flow],
    linewidths=[3 if n in flagged else 1 for n in flow],
    node_size=900, font_color="white", arrows=True,
)
plt.title("Likely same-owner clusters (colour) and high fan-out (red outline)")
plt.axis("off")
plt.savefig("clusters.png", dpi=150, bbox_inches="tight")
print("Clusters:", [sorted(c) for c in clusters if len(c) > 1])
print("Flagged for review:", sorted(flagged))

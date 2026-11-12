# Address Clustering (Common-Input Heuristic)

A small Python exploration of blockchain forensics, built on Nov 12, 2026 to learn how addresses are grouped by likely owner.

Uses networkx on a toy transaction list. If addresses are spent together as inputs in one transaction, they probably share an owner, so they are linked in a graph and each connected group is a cluster.

Run: `pip install networkx` then `python address_clustering.py`
## Mini Blockchain
`mini_blockchain.py`: a from-scratch blockchain in Python using SHA-256 hash linking and proof-of-work mining, with tamper detection. Built Nov 12, 2026 as a learning exercise. Run: `python mini_blockchain.py`
## Visualizer: design thinking
Built Nov 12, 2026 as a prototype.

**User:** a forensic analyst who must quickly see which addresses belong together and which deserve a closer look.
**Design decisions:** colour shows cluster membership, a red outline marks unusual behaviour, and unlinked addresses are grey so they don't compete for attention.
**Explainability:** every flag has a stated rule (fan-out of 3 or more), so the analyst can see why something was flagged instead of trusting a black box.
**Data science:** graph analysis with networkx; the next step is real Bitcoin data and more heuristics.

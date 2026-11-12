# Address Clustering (Common-Input Heuristic)

A small Python exploration of blockchain forensics, built on Nov 12, 2026 to learn how addresses are grouped by likely owner.

Uses networkx on a toy transaction list. If addresses are spent together as inputs in one transaction, they probably share an owner, so they are linked in a graph and each connected group is a cluster.

Run: `pip install networkx` then `python address_clustering.py`
## Mini Blockchain
`mini_blockchain.py`: a from-scratch blockchain in Python using SHA-256 hash linking and proof-of-work mining, with tamper detection. Built Nov 12, 2026 as a learning exercise. Run: `python mini_blockchain.py`

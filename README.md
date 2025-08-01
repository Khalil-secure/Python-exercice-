🧮 Python Dijkstra Exercise
This project is a Python implementation of Dijkstra's algorithm, designed to find the shortest path from point A to point B in a weighted graph. The goal is to accumulate the smallest possible total value while navigating through connected nodes.

🎓 Background
This exercise was developed during my engineering studies as part of learning graph theory and algorithmic programming. It reflects my early exploration of algorithmic problem-solving and my enthusiasm for sharing knowledge with the developer community.

🧠 How It Works
The graph is represented using matrices, where each cell indicates the weight (or cost) of the edge between two nodes.
The algorithm starts from a chosen node and iteratively updates the shortest known distances to all other nodes.
A recurrence function is used to update the matrix until the final form reveals the shortest path from the start node to any other node.
⚠️ Limitations
This implementation uses a matrix-based representation, which is not optimized for large graphs due to memory and performance constraints.
It is best suited for small to medium-sized graphs with clearly defined edge weights.

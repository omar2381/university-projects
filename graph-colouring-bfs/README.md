# Graph Algorithms: Colouring and Shortest Paths

Graph algorithms implemented on top of NetworkX.

University coursework on graph theory.

## Contents

| File | Algorithm |
|---|---|
| `greedy_col.py` | Greedy vertex colouring: visit vertices in order and give each the smallest colour not used by its neighbours. Draws the coloured graph with Matplotlib |
| `greedy_col_variation.py` | Greedy colouring with a different vertex order, where `find_next_vertex` chooses which vertex to colour next |
| `breadth_first.py` | Breadth-first search that labels vertices by their distance from a start vertex, giving the shortest-path distance between two vertices in an unweighted graph |

## Running it

```bash
pip install networkx matplotlib
python breadth_first.py
```

The scripts import test graphs from modules named `graph1.py` to `graph10.py`. These were provided with the course and are not included here, so supply your own module that defines a `Graph()` function returning a NetworkX graph.

## Tech

Python, NetworkX, Matplotlib

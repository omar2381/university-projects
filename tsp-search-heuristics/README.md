# Travelling Salesman Heuristics

Two local-search heuristics for the travelling salesman problem (find the shortest round trip that visits every city once), each with a basic and an enhanced version.

University coursework on AI search. Each run had a 60-second time limit, so the searches stop improving after 57 seconds and return the best tour found so far.

## Algorithms

| File | Algorithm | Starting tour |
|---|---|---|
| `AlgBbasic.py` | 2-opt | Cities in index order |
| `AlgBenhanced.py` | 2-opt | Greedy (nearest-neighbour style) |
| `AlgAbasic.py` | Lin-Kernighan style: combines 2-opt and 3-opt moves | Cities in index order |
| `AlgAenhanced.py` | Lin-Kernighan style: combines 2-opt and 3-opt moves | Greedy (nearest-neighbour style) |

- **2-opt** repeatedly reverses a segment of the tour whenever doing so shortens it, which removes crossing edges.
- **3-opt** considers reconnecting three edges instead of two.
- **The Lin-Kernighan style search** tries both kinds of move at each step and keeps whichever is better.
- **The enhanced versions** start from a greedy tour rather than an arbitrary one, so the local search begins closer to a good solution.

## Running it

The input parsing and the tour-file output are the course-provided template. The scripts expect that assignment's layout:

- a `city-files/` folder containing distance matrices in the course format (`NAME = ..., SIZE = ..., <distances>`);
- `alg_codes_and_tariffs.txt` in the parent folder.

```bash
python AlgBenhanced.py AISearchfile012.txt
```

The best tour and its length are written to a timestamped text file.

## Tech

Python (standard library only)

# DNA Sequence Alignment

Aligns two DNA sequences so that matching bases line up, inserting gaps (`-`) where needed, and compares a brute-force approach with dynamic programming.

University coursework on computational thinking.

## Scoring

| Pair | Score |
|---|---|
| A matched with A | +3 |
| C with C, or T with T | +2 |
| G matched with G | +1 |
| Mismatch | -3 |
| Base against a gap | -4 |

## Contents

| File | Approach |
|---|---|
| `ObjectiveOne.py` | **Brute force.** Recursively generates every possible alignment, scores each, and returns the best. Exponential time, so only practical for short sequences, but guaranteed optimal. |
| `ObjectiveTwo.py` | **Dynamic programming (local alignment, Smith-Waterman style).** Fills a score matrix in O(n x m) time and traces back from the highest cell to recover the best-matching region. Handles sequences far longer than the brute-force version. |
| `ObjectiveThree.py` | **Unfinished.** A start on processing a distance matrix between several sequences, a first step towards building a phylogenetic tree. It does not run to completion. |

Objectives one and two print the alignment, its score and the time taken.

## Running it

```bash
python ObjectiveTwo.py seq1.txt seq2.txt
```

Each input file contains one DNA sequence (letters `A`, `C`, `G`, `T`).

## Tech

Python (standard library only)

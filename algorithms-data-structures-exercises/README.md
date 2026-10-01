# Algorithms and Data Structures Exercises

Four short Python exercises from an algorithms and data structures module:
hash table probing, digit-factorial cycles, longest palindromic substring, and
a k-way quicksort.

## q1.py — open addressing

Two collision strategies on a table of size 23 with the hash `(4k + 7) mod 23`:

- `hash_quartic` probes at `(4k + 7) + i^4` for increasing `i`.
- `hash_double` uses a second hash, `17 - (k mod 17)`, as the step.

Both give up after 23 probes and return the table as it stands, so a full table
cannot loop forever.

## q2.py — digit-factorial cycles

Repeatedly replaces a number with the sum of the factorials of its digits
(0! to 9! come from a lookup table) and counts the steps until a value repeats.
Every starting number eventually enters a cycle; the count is how long it takes
to get there.

## q3.py — longest palindromic substring

Expand-around-centre, written three ways: `LP` for even-length centres, `LOP`
for odd-length ones, and `LP2` combining them. Each returns the length of the
longest palindrome in the string.

## kWaysQS.py — k-way quicksort

Reads integers from a file given on the command line and sorts them. Rather
than splitting around one pivot, `partition` chooses `k` pivots, sorts them with
insertion sort and divides the input into `k + 1` buckets, then recurses into
each. Arrays shorter than the pivot count fall back to insertion sort.

```bash
python kWaysQS.py numbers.txt 3
```

## Note

University coursework, kept as it was submitted. The code is deliberately
unchanged, so it reads as first- and second-year work: single-letter names,
manual loops in place of the standard library, and no tests.

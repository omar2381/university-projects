# Connect 4 with Rotating Rows (C)

A two-player, terminal-based variant of Connect 4 written in C.

University coursework (my first C project).

## Rules

- Players `x` and `o` take turns dropping a token into a column, and it falls to the lowest empty space.
- After dropping, the player may **rotate a row** one step left or right (`0` for no rotation). Tokens then fall again under gravity, so one move can rearrange the board.
- The board **wraps around horizontally**, so a line of four can continue from the right edge onto the left edge.
- The first player to line up four tokens wins.

## Implementation notes

- The board is an opaque `struct` behind the interface in `connect4.h`: setup, cleanup, reading and writing boards, validating and playing moves, and detecting a winner. It is sized from whatever board is in `initial_board.txt`.
- The board is allocated dynamically and freed at the end of the game.
- The final board is written to `final_board.txt`.

## Building and running

```bash
gcc -Wall -std=c11 -o connect4 main.c connect4.c
./connect4
```

To run the provided test, which plays scripted moves and compares the result with an expected board:

```bash
bash test_script.sh
```

## Tech

C11

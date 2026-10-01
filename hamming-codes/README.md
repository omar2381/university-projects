# Hamming Codes

Error-correcting codes implemented in Python: a repetition code and general Hamming codes, which are designed to detect and correct a single flipped bit in each codeword.

University coursework on coding theory.

## Functions

| Function | Purpose |
|---|---|
| `hammingGeneratorMatrix(r)` | Builds the generator matrix of the [2^r - 1, 2^r - r - 1] Hamming code |
| `message(a)` | Pads raw data into a message of the right length, including a length header |
| `hammingEncoder(m)` | Encodes a message into a codeword |
| `hammingDecoder(v)` | Computes the syndrome with the parity-check matrix and flips the bit it points to |
| `messageFromCodeword(c)` | Recovers the message from a codeword |
| `dataFromMessage(m)` | Strips the header and padding to recover the original data |
| `repetitionEncoder(m, n)` / `repetitionDecoder(v)` | Repetition code with majority-vote decoding |

## Usage

```python
from hamming import *

m = message([1, 0, 1])     # [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
dataFromMessage(m)         # [1, 0, 1]

c = hammingEncoder([1, 0, 1, 1])
messageFromCodeword(c)     # [1, 0, 1, 1]
```

## Known issue

`hammingDecoder` does not currently recover the codewords produced by `hammingEncoder`. The decoder's parity-check matrix uses a different bit ordering from the encoder's generator matrix. It also flips a bit when the syndrome is zero (no error), where it should leave the codeword unchanged.

## Tech

Python (standard library only)

# Lab 01 — Proof of Work

## Objective

Find the first nonce that makes the SHA-256 hash of `Jiaming-Luo` followed by the nonce's decimal digits begin with at least four zeroes. Repeat the search from zero with a five-zero target. The input contains no separator between the nickname and the nonce.

This lab illustrates the cost of producing a proof of work and the ease of checking it. The search hashes successive inputs until a digest matches the target prefix. A verifier can hash the reported input once and check the prefix. Establishing that the reported nonce was the *first* match requires checking the earlier candidates as well.

## Run the lab

Use Python 3. The lab uses only the standard library. From the repository root, run the official submission script.

```sh
python -B 01-proof-of-work/pow.py
```

The script runs both difficulties and prints the original input, the full hash, the nonce, the search time in seconds, and the number of attempts for each run. It also prints the difference in search time. `pow.py` and `test_pow.py` are the submission files. `pow_v2.py` is a separate prompt experiment kept outside the submission.

## Experiment results

These values come from one run of `pow.py` with Python 3.13.7.

| Difficulty | Original hash input | Full SHA-256 digest | Nonce | Attempts | Search time (s) |
| --- | --- | --- | ---: | ---: | ---: |
| 4 | `Jiaming-Luo57308` | `00003a88169ed4efb80491051b09896be3d4c40a7e25cb0111876be8eab89815` | 57,308 | 57,309 | 0.030019 |
| 5 | `Jiaming-Luo410551` | `000001ff9ecf2a69a23aa8951627e5fe49f995de8dd42127035f90d2881e6038` | 410,551 | 410,552 | 0.223174 |

## Difficulty and search time

Each hexadecimal digit has 16 possible values. If SHA-256 digests are modeled as uniformly distributed, an attempt has probability `1 / 16**difficulty` of meeting the target. This gives an expected 65,536 attempts at difficulty 4 and 1,048,576 at difficulty 5. Each additional leading zero multiplies the expected work by 16.

For this nickname, difficulty 5 took about 7.16 times as many attempts and 7.43 times as long in the measured run. The program reported an elapsed-time difference of 0.193156 seconds. The expected work describes an average across searches. For a fixed nickname and search order, the first matching nonce and attempt count are repeatable, while elapsed time can vary with the machine and its workload.

## Python concepts

- `calculate_hash(nickname, nonce)` uses an f-string to build the input, encodes it as UTF-8 bytes, and calls `hashlib.sha256(...).hexdigest()` to get a 64-character hexadecimal digest.
- `mine_pow(nickname, difficulty)` validates that the difficulty is an integer from 0 to 64 and rejects Boolean values. String repetition builds the target prefix, and `str.startswith()` checks each digest. At difficulty 0 the prefix is empty, so the first attempt succeeds.
- A `while` loop tries nonces in order. The function returns a tuple containing the nonce, digest, elapsed seconds, and attempt count. The attempt count is `nonce + 1` because the search starts at zero.
- `time.perf_counter()` measures the search loop. The `if __name__ == "__main__"` guard allows tests to import the functions without running the experiment.

## Tests

From the repository root, run the standard-library test suite.

```sh
python -B -m unittest discover -s 01-proof-of-work -v
```

The five tests in `test_pow.py` check a known SHA-256 digest, the first matching nonce for a small target and its associated results, the zero-difficulty case, out-of-range integers, and invalid types. Running `pow.py` separately exercises the two assignment difficulties.

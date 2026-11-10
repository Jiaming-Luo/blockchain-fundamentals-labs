import hashlib
import time


def calculate_hash(nickname, nonce):
    """Return the SHA-256 hex digest of the nickname followed by the nonce."""
    message = f"{nickname}{nonce}"
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def mine_pow(nickname, difficulty):
    """Return the first matching nonce, its hash, elapsed seconds, and attempts."""
    if isinstance(difficulty, bool) or not isinstance(difficulty, int):
        raise TypeError("difficulty must be an integer")
    if not 0 <= difficulty <= 64:
        raise ValueError("difficulty must be between 0 and 64")

    target = "0" * difficulty
    nonce = 0
    start = time.perf_counter()

    while True:
        hash_value = calculate_hash(nickname, nonce)
        if hash_value.startswith(target):
            elapsed = time.perf_counter() - start
            return nonce, hash_value, elapsed, nonce + 1
        nonce += 1


def main():
    nickname = "Jiaming-Luo"
    elapsed_by_difficulty = {}

    for difficulty in (4, 5):
        nonce, hash_value, elapsed, attempts = mine_pow(nickname, difficulty)
        elapsed_by_difficulty[difficulty] = elapsed
        print(f"Nickname: {nickname}, difficulty: {difficulty}")
        print(f"  Hash input: {nickname}{nonce}")
        print(f"  Nonce: {nonce}")
        print(f"  Hash: {hash_value}")
        print(f"  Elapsed: {elapsed:.6f} seconds")
        print(f"  Attempts: {attempts}")

    difference = elapsed_by_difficulty[5] - elapsed_by_difficulty[4]
    print(f"Elapsed difference (difficulty 5 minus 4): {difference:+.6f} seconds")


if __name__ == "__main__":
    main()

"""Walk a bit stream one step at a time: 1 = step right, 0 = step left."""
import random


def bits(n, seed=None):
    rng = random.Random(seed)
    return [rng.randint(0, 1) for _ in range(n)]


def walk(stream):
    pos, path = 0, [0]
    for b in stream:
        pos += 1 if b else -1
        path.append(pos)
    return path


if __name__ == "__main__":
    print(walk(bits(64, seed=None))[-1])

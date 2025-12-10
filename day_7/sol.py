#!/usr/bin/env python3
from typing import List

INPUT_FILE = 'input.txt'


def count_splits(start_idx: int, manifold: List[str]) -> int:
    beams = {start_idx}
    splits = 0
    for row in manifold:
        splitters = {i for i, x in enumerate(row) if x == '^' }
        new_beams = set()
        for beam in beams:
            if beam in splitters:
                splits += 1
                if beam > 0:
                    new_beams.add(beam - 1)
                if beam < len(row) - 1:
                    new_beams.add(beam + 1)
            else:
                new_beams.add(beam)

        beams = new_beams

    return splits


def main():
    with open(INPUT_FILE, mode='r') as f:
        start_idx = next(f).index('S')
        manifold = f.read().split('\n')
        print(f"Part I: {count_splits(start_idx, manifold)}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import re
import numpy as np
from typing import List, Sequence

INPUT_FILE = 'input.txt'


def calc(nums: Sequence[Sequence[int]], ops: List[str]) -> int:
    tot = 0
    for row, op in zip(nums, ops):
        if op == '+':
            tot += sum(row)
        else:
            tot += np.prod(row)

    return tot


def main():
    with open(INPUT_FILE, mode='r') as f:
        txt = f.read().rstrip().split('\n')

        nums = np.array([list(map(int, filter(len, re.split(r"\s+", x)))) for x in txt[:-1]]).T
        ops = re.split(r'\s+', txt[-1])

        print(f"Part I: {calc(nums, ops)}")

        nums = [reversed(x) for x in txt[:-1]]
        nums = list(map(list, zip(*nums)))
        nums = '\n'.join([''.join(x) for x in nums])
        nums = [x.split('\n') for x in re.split(r"\n\s+\n", nums)]
        nums = [list(map(int, filter(len, x))) for x in nums]

        print(f"Part II: {calc(nums, reversed(ops))}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import re
import numpy as np
# from typing import List, Tuple

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, mode='r') as f:
        txt = f.read().rstrip().split('\n')
        nums = txt[:-1]
        ops = txt[-1]

        nums = np.array([list(map(int, filter(len, re.split(r"\s+", x)))) for x in nums]).T
        ops = re.split(r'\s+', ops)

        tot = 0
        for row, op in zip(nums, ops):
            if op == '+':
                tot += sum(row)
            else:
                tot += np.prod(row)

        print(f"Part I: {tot}")


if __name__ == '__main__':
    main()

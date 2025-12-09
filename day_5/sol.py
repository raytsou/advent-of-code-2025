#!/usr/bin/env python3
from typing import List, Tuple

INPUT_FILE = 'input.txt'


def count_fresh(ranges: List[Tuple[int]], ingredients: List[int]) -> int:
    fresh_cnt = 0
    for ingredient in ingredients:
        for lower, upper in ranges:
            if lower <= ingredient <= upper:
                fresh_cnt += 1
                break

    return fresh_cnt


def count_size(ranges: List[Tuple[int]]) -> int:
    ranges.sort()
    size = 0
    prev_upper = 0
    for lower, upper in ranges:
        if lower <= prev_upper:
            size += max(upper - prev_upper, 0)
        else:
            size += upper - lower + 1
        prev_upper = upper

    return size


def main():
    with open(INPUT_FILE, mode='r') as f:
        ranges, ingredients = [x.rstrip().split('\n') for x in f.read().split("\n\n")]
        ranges = [tuple(map(int, x.split('-'))) for x in ranges]
        ingredients = [int(x) for x in ingredients]

        print(f"Part I: {count_fresh(ranges, ingredients)}")
        print(f"Part II: {count_size(ranges)}")


if __name__ == '__main__':
    main()

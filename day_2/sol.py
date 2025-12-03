#!/usr/bin/env python3
from typing import Set

INPUT_FILE = 'input.txt'


def get_invalids(repeat_times: int, beg: str, end: str) -> Set[int]:
    start = str(10 ** len(beg))
    curr = start[:len(start)//repeat_times] * repeat_times

    invalid = set()
    while int(curr) <= int(end):
        if int(curr) >= int(beg):
            invalid.add(int(curr))

        base = int(curr[:len(curr)//repeat_times])
        curr = str(base + 1)[:len(curr)] * repeat_times

    return invalid


def main():
    invalid_doubles = set()
    invalid_repeats = set()
    with open(INPUT_FILE, mode='r') as f:
        for range_str in f.read().rstrip().split(','):
            begin, end = range_str.split("-")
            invalid_doubles = invalid_doubles.union(get_invalids(2, begin, end))
            invalid_repeats = invalid_repeats.union(invalid_doubles)
            for i in range(3, len(end)+1):
                invalid_repeats = invalid_repeats.union(get_invalids(i, begin, end))

    print(f"Part I: {sum(invalid_doubles)}")
    print(f"Part II: {sum(invalid_repeats)}")


if __name__ == '__main__':
    main()

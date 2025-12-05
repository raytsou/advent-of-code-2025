#!/usr/bin/env python3
from typing import List

INPUT_FILE = 'input.txt'


def calculate_largest_joltage(bank: List[int]) -> int:
    jolts = max(bank[:-1])
    idx = bank.index(jolts)
    jolts *= 10
    jolts += max(bank[idx+1:])
    return jolts


def main():
    total = 0
    with open(INPUT_FILE, mode='r') as f:
        for bank in f:
            total += calculate_largest_joltage([int(x) for x in bank if x.isdigit()])

    print(f"Part I: {total}")


if __name__ == '__main__':
    main()

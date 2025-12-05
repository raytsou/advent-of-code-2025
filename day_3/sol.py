#!/usr/bin/env python3
from typing import List

INPUT_FILE = 'input.txt'


def calculate_largest_joltage(bank: List[int], cnt: int) -> int:
    if cnt <= 1:
        return max(bank)

    # print(bank[:1-cnt])
    jolts = max(bank[:1-cnt])
    idx = bank.index(jolts)
    jolts *= 10 ** (cnt-1)
    jolts += calculate_largest_joltage(bank[idx+1:], cnt-1)
    return jolts


def main():
    total_double = 0
    total_dozen = 0
    with open(INPUT_FILE, mode='r') as f:
        for bank in f:
            batteries = [int(x) for x in bank if x.isdigit()]
            total_double += calculate_largest_joltage(batteries, 2)
            total_dozen += calculate_largest_joltage(batteries, 12)

    print(f"Part I: {total_double}")
    print(f"Part II: {total_dozen}")


if __name__ == '__main__':
    main()

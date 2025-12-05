#!/usr/bin/env python3
from typing import List

INPUT_FILE = 'input.txt'


def get_footprint_cost(diagram: List[List[bool]], row: int, col: int) -> int:
    cost = 0
    for i in range(max(0, row-1), min(len(diagram), row+2)):
        r = diagram[i]
        cost += sum(r[max(0, col-1):min(len(diagram[0]), col+2)])

    return cost


def calculate_accessible(diagram: List[List[bool]]) -> int:
    accessible = set()
    for i, row in enumerate(diagram):
        for j, el in enumerate(row):
            if el and (get_footprint_cost(diagram, i, j) < 5):
                accessible.add((i, j))

    return len(accessible)


def main():
    with open(INPUT_FILE, mode='r') as f:
        diagram = list()
        for row in f:
            diagram.append([True if x == "@" else False for x in row.rstrip()])

        print(f"Part I: {calculate_accessible(diagram)}")


if __name__ == '__main__':
    main()

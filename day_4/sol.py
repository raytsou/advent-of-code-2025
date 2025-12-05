#!/usr/bin/env python3
from typing import List, Set

INPUT_FILE = 'input.txt'


def get_footprint_cost(diagram: List[List[bool]], row: int, col: int) -> int:
    cost = 0
    for i in range(max(0, row-1), min(len(diagram), row+2)):
        r = diagram[i]
        cost += sum(r[max(0, col-1):min(len(diagram[0]), col+2)])

    return cost


def get_accessible(diagram: List[List[bool]]) -> Set[int]:
    accessible = set()
    for i, row in enumerate(diagram):
        for j, el in enumerate(row):
            if el and (get_footprint_cost(diagram, i, j) < 5):
                accessible.add((i, j))

    return accessible


def main():
    accessible_cnt = 0
    with open(INPUT_FILE, mode='r') as f:
        diagram = list()
        for row in f:
            diagram.append([True if x == "@" else False for x in row.rstrip()])

        accessible = get_accessible(diagram)
        accessible_cnt = len(accessible)
        print(f"Part I: {accessible_cnt}")

        while accessible:
            for i, j in accessible:
                diagram[i][j] = False

            accessible = get_accessible(diagram)
            accessible_cnt += len(accessible)

        print(f"Part II: {accessible_cnt}")


if __name__ == '__main__':
    main()

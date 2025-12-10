#!/usr/bin/env python3
from dataclasses import dataclass
from typing import (
    List,
    Self,
)

INPUT_FILE = 'input.txt'


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __lt__(self, other: Self):
        return (self.x < other.x or self.y < other.y or self.z < other.z)

    def distance_to(self, other: Self) -> float:
        return (
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        ) ** 0.5


class JunctionMap:
    def __init__(self, points: List[Point]):
        self.__points = points
        self.__dists = dict()
        for i, pt1 in enumerate(points):
            for pt2 in points[i+1:]:
                pair = (pt1, pt2) if pt1 < pt2 else (pt2, pt1)
                self.__dists[pair] = pt1.distance_to(pt2)

    def connect(self, connections: int) -> int:
        if connections < 0:
            connections = len(self.__dists)

        cliques = dict()
        cidx = 0
        clique_map = {p: None for p in self.__points}
        closest_dists = sorted(self.__dists, key=self.__dists.get)[:connections]
        for pt1, pt2 in closest_dists:
            c1_id = clique_map[pt1]
            c2_id = clique_map[pt2]

            if c1_id is not None:
                if c2_id is not None:
                    if c1_id == c2_id:
                        continue

                    c2 = cliques[c2_id]
                    for pt in c2:
                        clique_map[pt] = c1_id

                    cliques[c1_id] = cliques[c1_id].union(c2)
                    cliques.pop(c2_id)
                else:
                    cliques[c1_id].add(pt2)
                    clique_map[pt2] = c1_id
            else:
                if c2_id is not None:
                    cliques[c2_id].add(pt1)
                    clique_map[pt1] = c2_id
                else:
                    cliques[cidx] = {pt1, pt2}
                    clique_map[pt1] = cidx
                    clique_map[pt2] = cidx
                    cidx += 1

            if (
                len(cliques) == 1 and
                None not in clique_map.values()
            ):
                return pt1.x * pt2.x

        ret = 1
        for i in range(3):
            idx = max(cliques, key=lambda x: len(cliques.get(x)))
            ret *= len(cliques[idx])
            cliques.pop(idx)
        return ret


def main():
    with open(INPUT_FILE, mode='r') as f:
        pts = [Point(*map(int, x.split(','))) for x in f.read().split('\n')]
        m = JunctionMap(pts)
        print(f"Part I: {m.connect(1000)}")
        print(f"Part II: {m.connect(-1)}")


if __name__ == '__main__':
    main()

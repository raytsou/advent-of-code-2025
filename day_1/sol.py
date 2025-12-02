#!/usr/bin/env python3

INPUT_FILE = 'input.txt'


class Dial:
    RANGE = 100

    def __init__(self):
        self.__val = 50

    def rotate(self, direction: str, distance: int) -> None:
        match(direction):
            case 'L':
                self.__val = (self.__val - distance) % self.RANGE
            case 'R':
                self.__val = (self.__val + distance) % self.RANGE

    def get_zero_crossover_count(self, direction: str, distance: int) -> int:
        match(direction):
            case 'L':
                return (distance - self.__val + 99) // self.RANGE - (self.__val == 0)
            case 'R':
                return (distance + self.__val - 1) // self.RANGE

    @property
    def value(self) -> int:
        return self.__val


def main():
    dial = Dial()
    zero_cnt = 0
    zero_crosses = 0
    with open(INPUT_FILE, mode='r') as f:
        for rotation in f:
            direction = rotation[0]
            distance = int(rotation[1:])

            x = dial.get_zero_crossover_count(direction, distance)
            zero_crosses += x
            dial.rotate(direction, distance)

            if (dial.value == 0):
                zero_cnt += 1

    print(f"Part I: {zero_cnt}")
    print(f"Part II: {zero_cnt + zero_crosses}")


if __name__ == '__main__':
    main()

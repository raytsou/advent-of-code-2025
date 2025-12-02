#!/usr/bin/env python3

INPUT_FILE = 'input.txt'


class Dial:
    RANGE = 100

    def __init__(self):
        self.__val = 50

    def rotate(self, direction: str, num: int) -> None:
        match(direction):
            case 'L':
                self.__val = (self.__val - num) % self.RANGE
            case 'R':
                self.__val = (self.__val + num) % self.RANGE

    @property
    def value(self) -> int:
        return self.__val


def main():
    dial = Dial()
    zero_cnt = 0
    with open(INPUT_FILE, mode='r') as f:
        for rotation in f:
            direction = rotation[0]
            distance = int(rotation[1:])
            dial.rotate(direction, distance)

            if (dial.value == 0):
                zero_cnt += 1

    print(zero_cnt)


if __name__ == '__main__':
    main()

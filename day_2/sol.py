#!/usr/bin/env python3

INPUT_FILE = 'input.txt'


def sum_doubles(beg: str, end: str) -> int:
    beg_digits = len(beg)
    if (beg_digits % 2):
        beg = str(10 ** beg_digits)

    end_digits = len(end)
    if end_digits % 2:
        end = str(10 ** (end_digits - 1) - 1)

    beg_half1 = beg[:len(beg)//2]
    beg_half2 = beg[len(beg)//2:]

    beg = beg_half1 * 2
    if beg_half1 < beg_half2:
        beg = str(int(beg_half1) + 1) * 2

    end_half1 = end[:len(end)//2]
    end_half2 = end[len(end)//2:]
    end = end_half1 * 2
    if end_half1 > end_half2:
        end = str(int(end_half1) - 1) * 2

    running_sum = 0
    while int(beg) <= int(end):
        running_sum += int(beg)
        half = int(beg[:len(beg)//2])
        beg = str(half + 1) * 2

    return running_sum


def main():
    invalid_sum = 0
    with open(INPUT_FILE, mode='r') as f:
        for range_str in f.read().rstrip().split(','):
            begin, end = range_str.split("-")
            invalid_sum += sum_doubles(begin, end)

    print(f"Part I: {invalid_sum}")


if __name__ == '__main__':
    main()

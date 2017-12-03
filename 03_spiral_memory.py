import numpy as np


def find_closest(number, max_spiral_num):
    """Part 2"""

    def count(a, i, j):

        def try_get_value(i, j):
            if len(a) > abs(i) and len(a[i]) > abs(j):
                return a[i][j]
            else:
                return 0

        return (try_get_value(i + 1, j) + try_get_value(i + 1, j + 1) +
                try_get_value(i, j + 1) + try_get_value(i - 1, j + 1) +
                try_get_value(i - 1, j) + try_get_value(i - 1, j - 1) +
                try_get_value(i, j - 1) + try_get_value(i + 1, j - 1))

    # lol should be enough
    size = 2 * max_spiral_num + 1
    zeros = np.zeros((size, size), dtype=np.int)
    zeros[0][0] = 1
    spiral_num = 0
    j = 0
    # No ckeck for  index out of range
    while True:
        spiral_num += 1
        i = spiral_num
        side = (2 * spiral_num + 1)
        for j in range(j, j + side - 1, 1):
            zeros[spiral_num][j] = count(zeros, spiral_num, j)
            if zeros[spiral_num][j] > number:
                return zeros[spiral_num][j]
        for i in range(i - 1, i - side, -1):
            zeros[i][j] = count(zeros, i, j)
            if zeros[i][j] > number:
                return zeros[i][j]
        for j in range(j - 1, j - side, -1):
            zeros[i][j] = count(zeros, i, j)
            if zeros[i][j] > number:
                return zeros[i][j]
        for i in range(i + 1, i + side, 1):
            zeros[i][j] = count(zeros, i, j)
            if zeros[i][j] > number:
                return zeros[i][j]


def find_distance(number):
    """Part 1"""
    if number == 1:
        return 0
    spiral_num = 0
    while True:
        spiral_num += 1
        side = (2 * spiral_num + 1)
        maximum = side * side
        minimum = maximum - (4 * (side - 1)) + 1
        if minimum <= number <= maximum:
            anchor = minimum + (side - 1) / 2 - 1
            for i in range(0, 4):
                anchor += i * side - i
                if anchor - (
                    (side - 1) / 2 - 1) <= number <= anchor + (side - 1) / 2:
                    return spiral_num + abs(anchor - number), spiral_num


def main():
    distance, spiral_num = find_distance(265149)
    print('Part 1: ' + str(distance))
    print('Part 2: ' + str(find_closest(265149, spiral_num)))


if __name__ == '__main__':
    main()
from os import path

PWD = path.dirname(path.realpath(__file__))
FILE_NAME = 'input.txt'


def read_input(file_name=path.join(PWD, FILE_NAME)):
    content = []
    with open(file_name) as file:
        for line in file:
            content.append(list(map(int, line.split())))
    return content


def find_checksum(data, part=1):

    def part_1(row):
        return max(row) - min(row)

    def part_2(row):
        sorted_row = sorted(row)
        for i in range(len(sorted_row) - 1, 1, -1):
            for j, _ in enumerate(sorted_row):
                if j < i and sorted_row[i] % sorted_row[j] == 0:
                    return sorted_row[i] / sorted_row[j]
        return

    solution = 0
    if part == 1:
        for row in data:
            solution += part_1(row)
    else:
        for row in data:
            solution += part_2(row)
    return solution


def main():
    data = read_input()
    print('Part 1: ' + str(find_checksum(data)))
    print('Part 2: ' + str(find_checksum(data, 2)))


if __name__ == '__main__':
    main()
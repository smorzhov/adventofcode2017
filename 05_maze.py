from os import path

PWD = path.dirname(path.realpath(__file__))
FILE_NAME = 'input.txt'


def read_input(file_name=path.join(PWD, FILE_NAME)):
    content = []
    with open(file_name) as file:
        for line in file:
            content.append(int(line))
    return content


def count_steps(data, part=1):
    steps = 0
    i = 0
    while i >= 0 and i < len(data):
        current_value = data[i]
        if part == 2 and data[i] >= 3:
            data[i] -= 1
        else:
            data[i] += 1
        i += current_value
        steps += 1
    return steps


def main():
    print('Part 1: ' + str(count_steps(read_input())))
    print('Part 2: ' + str(count_steps(read_input(), 2)))


if __name__ == '__main__':
    main()
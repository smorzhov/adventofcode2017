from os import path

PWD = path.dirname(path.realpath(__file__))
FILE_NAME = 'input.txt'


def read_input(file_name=path.join(PWD, FILE_NAME)):
    content = []
    with open(file_name) as file:
        for line in file:
            content.append(list(line.split()))
    return content


def count_valid_passphrases(data, part=1):
    unique = 0
    for row in data:
        if len(row) == len(set(row)):
            if part == 1:
                unique += 1
            else:
                if len(row) == len(set(map(lambda word: ''.join(sorted(word)), row))):
                    unique += 1
    return unique


def main():
    data = read_input()
    print('Part 1: ' + str(count_valid_passphrases(data)))
    print('Part 2: ' + str(count_valid_passphrases(data, 2)))


if __name__ == '__main__':
    main()
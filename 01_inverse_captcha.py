from os import path

PWD = path.dirname(path.realpath(__file__))
FILE_NAME = 'input.txt'

def read_input(file_name):
    with open(file_name) as f:
        return f.readline()


def find_solution(data, step=1):
    result = 0
    for i in range(0, len(data)):
        if data[i] == data[(i + step) % len(data)]:
            result += data[i]
    return result


def main():
    raw_data = read_input(path.join(PWD, FILE_NAME))
    try:
        data = list(map(int, list(raw_data)))
    except ValueError as ex:
        print(ex)
        return
    print('Part 1: ' + str(find_solution(data)))
    print('Part 2: ' + str(find_solution(data, int(len(data) / 2))))


if __name__ == '__main__':
    main()

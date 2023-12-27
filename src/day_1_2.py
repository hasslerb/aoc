import argparse

number_strings = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def extract_first(line: str) -> int:
    index = 0
    while True:
        if line[index].isnumeric():
            return int(line[index])
        else:
            for k in number_strings:
                if k in line[:index+1]:
                    return number_strings[k]
        index += 1

def extract_last(line: str) -> int:
    index = -1
    while True:
        if line[index].isnumeric():
            return int(line[index])
        else:
            for k in number_strings:
                if k in line[index:]:
                    return number_strings[k]
        index -= 1

def calculate_line(line: str) -> str:
    return extract_first(line) * 10 + extract_last(line)

def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            sum += calculate_line(line)

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)
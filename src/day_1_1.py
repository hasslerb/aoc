import argparse

def extract_numeric(line: str) -> str:
    return ''.join(x for x in line if x.isdigit())

def calculate_line(line: str) -> str:
    numeric_line = extract_numeric(line)
    first_digit = int(numeric_line[0])
    last_digit = int(numeric_line[-1])

    return first_digit * 10 + last_digit

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

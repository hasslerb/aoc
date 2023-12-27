import argparse
import re

def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            row = line.split(" ")
            print(row)
            row = [int(x) for x in row if len(x) > 0]

            last_values = []
            while True:
                new_row = []

                for i in range(1, len(row)):
                    new_row.append(row[i] - row[i-1])
                print(new_row)
                last_values.append(row[0])
                if len(new_row) == len([x for x in new_row if x == 0]):
                    break
                row = new_row

            new_val = 0
            for val in reversed(last_values):
                new_val = val - new_val
                print(new_val)

            sum += new_val

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)
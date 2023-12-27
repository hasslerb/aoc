import argparse
import re

def solve_puzzle(input):
    steps = 0
    with open(input, "r") as f:
        instructions = f.readline().rstrip()

        line = f.readline().rstrip()
        mapp = {}

        line = f.readline().rstrip()
        data = re.findall(r"\w+", line)
        start_location = data[0]
        while True:
            location, left, right = re.findall(r"\w+", line)
            mapp[location] = [left, right]

            line = f.readline().rstrip()
            if not line:
                break

        location = "AAA"

        while True:
            left_or_right = 0 if instructions[steps % len(instructions)] == "L" else 1
            # print (f" {location}  {mapp[location]}  {left_or_right} ")
            location = mapp[location][left_or_right]
            steps += 1
            if location == "ZZZ":
                break

    return steps

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

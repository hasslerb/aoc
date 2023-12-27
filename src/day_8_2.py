import argparse
import re
import math
from functools import reduce

def solve_puzzle(input):
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

        locations = [node for node in mapp.keys() if node[2] == "A"]
        steps = [0]*len(locations)

        i = 0
        for location in locations:
            while True:
                left_or_right = 0 if instructions[steps[i] % len(instructions)] == "L" else 1
                # print (f" {location}  {mapp[location]}  {left_or_right} ")
                location = mapp[location][left_or_right]
                steps[i] += 1
                if location[2] == "Z":
                    break
            i += 1

        print(steps)
    return reduce(lambda x,y:(x*y)//math.gcd(x,y),steps)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

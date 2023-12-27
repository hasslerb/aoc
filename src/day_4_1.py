import argparse
import re

def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            product = 0
            each = line.split("|")
            winners = re.findall(r"(\d+) ", each[0])
            winners = [int(winner) for winner in winners]
            print (each)
            print(f"  winners {winners}")
            ours = re.findall(r"(\d+)", each[1])
            ours = [int(our) for our in ours]
            print(f"  ours {ours}")
            for our in ours:
                if our in winners:
                    if product == 0:
                        product = 1
                    else:
                        product = product*2
            sum += product

    return sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)
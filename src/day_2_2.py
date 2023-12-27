import argparse
import re

color_quantities = {
    "blue": 14,
    "green": 13,
    "red": 12
}

def product_of_set(line):
    product = 1
    print(line)
    for color in color_quantities:
        pattern = r"(\d+) " + color + r"*"
        count = re.findall(pattern, line)
        print(f"  {color} counts: {count}")

        # Remove empties
        maximum = max([int(c) for c in count if c])
        print(f"     max: {maximum}")

        product = product*maximum
    print(product)
    return product

def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            sum += product_of_set(line)

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

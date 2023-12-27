import argparse
import re

def get_number_indices(line):
    pattern = r"(\d+)"
    numbers = re.findall(pattern, line)
    number_indices = []
    if numbers:
        ref_index = 0
        for number in numbers:
            start_index = line.index(number, ref_index)
            ref_index = start_index + len(number)
            number_indices.append((number, range(start_index, start_index+len(number))))
    print(f"number_indices {number_indices}")
    return number_indices

def get_symbol_indices(line):
    symbols = re.findall(r"([^A-Za-z0-9\\.])", line)
    indices = []
    if symbols:
        ref_index = 0
        for symbol in symbols:
            start_index = line.index(symbol, ref_index)
            ref_index = start_index + 1
            indices.append(start_index)
    print(f" symbols {indices}")
    return indices

def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        number_indices_list = []
        symbol_indices_list = []
        row_length = 0
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            row_length = len(line)
            number_indices_list.append(get_number_indices(line))
            symbol_indices_list.append(get_symbol_indices(line))

        for i in range(len(symbol_indices_list)):
            print(f"  {i}")
            for symbol_index in symbol_indices_list[i]:
                print(f"    {symbol_index}")
                adjacent_list = []
                lines = []
                if i-1 >= 0:
                    lines.append(i-1)
                lines.append(i)
                if i+1 < len(number_indices_list):
                    lines.append(i+1)
                print(f"    {symbol_index}, lines: {lines}")

                for line in lines:
                    for number_and_indices in number_indices_list[line]:
                        print(f"checking row {i} with symbol index {symbol_index} for number {number_and_indices[0]} of in row {line}")
                        if symbol_index > 0:
                            # print(f"  index-1")
                            if symbol_index-1 in number_and_indices[1] and number_and_indices not in adjacent_list:
                                adjacent_list.append(number_and_indices)

                        if symbol_index in number_and_indices[1] and number_and_indices not in adjacent_list:
                            adjacent_list.append(number_and_indices)

                        if symbol_index < row_length -1:
                            # print(f"  index+1")
                            if symbol_index+1 in number_and_indices[1] and number_and_indices not in adjacent_list:
                                adjacent_list.append(number_and_indices)

                print(f"     adj_list {adjacent_list}")
                if len(adjacent_list) == 2:

                    print(f"   found {adjacent_list}")
                    sum += (int(adjacent_list[0][0]) *  int(adjacent_list[1][0]))



    return sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)
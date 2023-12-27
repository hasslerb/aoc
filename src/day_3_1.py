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
    print(number_indices)
    return number_indices

def get_symbol_indices(line):
    symbols = re.findall(r"([^A-Za-z0-9\\.])", line)
    indices = []
    if symbols:
        ref_index = 0
        for symbol in symbols:
            start_index = line.index(symbol, ref_index)
            print(f"  {symbol}  {start_index}  {ref_index}")
            ref_index = start_index + 1
            indices.append(start_index)
    print(indices)
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

        for i in range(len(number_indices_list)):
            print(f"  {i}")
            for number in number_indices_list[i]:
                found = False
                for index in number[1]:
                    lines = []
                    if i-1 >= 0:
                        lines.append(i-1)
                    lines.append(i)
                    if i+1 < len(number_indices_list):
                        lines.append(i+1)

                    for line in lines:
                        print(f"checking {number[0]} of row {i} at index {index} in row {line} in {symbol_indices_list[line]}")
                        if index > 0:
                            print(f"  index-1")
                            if index-1 in symbol_indices_list[line]:
                                found = True
                                break
                        if index in symbol_indices_list[line]:
                            found = True
                            break

                        if index < row_length -1:
                            print(f"  index+1")
                            if index+1 in symbol_indices_list[line]:
                                found = True
                                break

                if found:
                    print(f"   found {number[0]}")
                    sum += int(number[0])

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

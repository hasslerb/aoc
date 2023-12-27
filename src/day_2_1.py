import argparse
import re

color_quantities = {
    "blue": 14,
    "green": 13,
    "red": 12
}

def split_sets(line):
    game_id_data = re.findall(r"Game (\d+):(.+)", line)[0]
    sets = game_id_data[1].split(";")
    return (int(game_id_data[0]), sets)

def check_set(sets):
    for set in sets:
        for color in color_quantities:
            pattern = r"(\d+) " + color
            count = re.findall(pattern, set)
            print(f"  {color}: {count}")
            if count and int(count[0]) > color_quantities[color]:
                return False
    return True


def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            game_id_set_data = split_sets(line)
            print (game_id_set_data)
            if check_set(game_id_set_data[1]):
                sum += game_id_set_data[0]

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

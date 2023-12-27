import argparse

def solve_puzzle(input):
    lowest = 10000000000
    with open(input, "r") as f:
        line = f.readline().rstrip()
        seeds = [int(x) for x in line.split(" ") if x.isnumeric()]
        print (seeds)

        mapping_id = -1
        mappings = []
        while True:
            line = f.readline()
            if not line:
                break
            line = line.rstrip()
            if "map" in line:
                mapping_id += 1
                mappings.append([])
            else:
                line_data = line.split(" ")
                if len(line_data) == 3:
                    mappings[mapping_id].append(list(map(lambda x: int(x), line_data)))


        print(mappings)

        for seed in seeds:
            mapped_id = seed
            for mapping in mappings:
                for sub_mapping in mapping:
                    dest_range_start, source_range_start, range_length = sub_mapping
                    difference = mapped_id - source_range_start
                    if 0 <= difference < range_length:
                        mapped_id = dest_range_start + difference
                        break
                    # print(f"  seed: {seed} -> {mapped_id}")
            print(f"seed: {seed}: {mapped_id}")
            lowest = min(lowest, mapped_id)
    return lowest

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

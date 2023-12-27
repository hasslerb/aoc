import argparse
import re
import functools

def solve_puzzle(input):
    sum = 0
    with open(input, "r") as f:
        instances = [0] + [1]*196 # count index 0 as irrelevant
        card = 1
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            wins = 0
            each = line.split("|")
            winners = re.findall(r"(\d+) ", each[0])
            winners = [int(winner) for winner in winners]
            # print (each)
            # print(f"  winners {winners}")
            ours = re.findall(r"(\d+)", each[1])
            ours = [int(our) for our in ours]
            # print(f"  ours {ours}")
            for our in ours:
                if our in winners:
                    wins += 1
            print(f"WIN COUNT {wins} for card {card}")
            for x in range(card+1,card+1+wins):
                if x < len(instances):
                    instances[x] += instances[card]
                else:
                    instances.append(instances[card])
            print(f"  instances {instances}")

            card += 1
        sum = functools.reduce(lambda a,b: a+b, instances)

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

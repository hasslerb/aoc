import argparse
import math

def solve_puzzle(input):
    product = 1
    with open(input, "r") as f:
        line = f.readline().rstrip()
        times = [int(x) for x in line.split(" ") if x.isnumeric()]
        line = f.readline().rstrip()
        distances = [int(x) for x in line.split(" ") if x.isnumeric()]

        for i in range(len(times)):

            a = -1
            b = times[i]
            c = 0-distances[i]

            d = b**2-4*a*c # discriminant
            if d == 0:
                x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
                # This is a tie
            else:
                x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
                x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)

                if x1 < x2:
                    if x1.is_integer():
                        x1 = x1 + 1
                    else:
                        x1 = math.ceil(x1)

                    if x2.is_integer():
                        x2 = x2 - 1
                    else:
                        x2 = math.floor(x2)
                    count = x2-x1+1
                else:
                    if x2.is_integer():
                        x2 = x2 + 1
                    else:
                        x2 = math.ceil(x2)

                    if x1.is_integer():
                        x1 = x1 - 1
                    else:
                        x1 = math.floor(x1)
                    count = x1-x2+1

                print(f" count {count},  {x1} {x2}")
                product = product * count

    return product

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)
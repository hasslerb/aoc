import argparse

matrix = []

galaxy_coordinates = []

def solve_puzzle(input):
    with open(input, "r") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            matrix.append(line)
            if "#" not in line:
                matrix.append(line)

    columns_without_galaxy = []
    for i in range(len(matrix[0])):
        for line in matrix:
            if "#" in line[i]:
                break
        else:
            columns_without_galaxy.append(i)

    for column_idx in reversed(columns_without_galaxy):
        for row_idx in range(len(matrix)):
            matrix[row_idx] = matrix[row_idx][:column_idx] + "." + matrix[row_idx][column_idx:]

    for row_idx in range(len(matrix)):
        for column_idx in range(len(matrix[0])):
            if matrix[row_idx][column_idx] == "#":
                galaxy_coordinates.append((row_idx, column_idx))

    sum = 0

    print(galaxy_coordinates)

    for i in range(len(galaxy_coordinates) - 1):
        for j in range(i+1, len(galaxy_coordinates)):
            horizontal_distance = abs(galaxy_coordinates[i][0] - galaxy_coordinates[j][0])
            vertical_distance = abs(galaxy_coordinates[i][1] - galaxy_coordinates[j][1])
            sum += horizontal_distance + vertical_distance

    return sum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

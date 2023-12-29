import argparse

EXPANSION = 999999

matrix = []
unexpanded_galaxy_coordinates = []
galaxy_coordinates = []

def solve_puzzle(input):
    with open(input, "r") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            matrix.append(line)

    rows_without_galaxy = []
    for i in range(len(matrix)):
        if "#" not in matrix[i]:
            rows_without_galaxy.append(i)

    columns_without_galaxy = []
    for i in range(len(matrix[0])):
        for line in matrix:
            if "#" in line[i]:
                break
        else:
            columns_without_galaxy.append(i)

    for row_idx in range(len(matrix)):
        for column_idx in range(len(matrix[0])):
            if matrix[row_idx][column_idx] == "#":
                unexpanded_galaxy_coordinates.append((row_idx, column_idx))

    print(rows_without_galaxy)
    print(columns_without_galaxy)

    for coordinate in unexpanded_galaxy_coordinates:
        row = coordinate[0]
        adjustment = 0
        for i in rows_without_galaxy:
            if row > i:
                adjustment += EXPANSION
        row += adjustment

        column = coordinate[1]
        adjustment = 0
        for i in columns_without_galaxy:
            if column > i:
                adjustment += EXPANSION
        column += adjustment

        galaxy_coordinates.append((row, column))
    print(unexpanded_galaxy_coordinates)
    print(galaxy_coordinates)

    sum = 0
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

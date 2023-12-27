import argparse

matrix = []

parts = { #L  R    D   U
    "|": ((0, 0 ), (1, -1)),
    "-": ((-1, 1), (0, 0)),
    "L": ((0, 1 ), (0, -1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((-1, 0), (1, 0)),
    "F": ((0, 1 ), (1, 0)),
    ".": ((0, 0 ), (0, 0)),
    "S": ((0, 0 ), (0, 0)),
}

def get_next_coordinates(prev_coordinates, coordinates):
    global matrix
    x = coordinates[0]
    y = coordinates[1]
    part = parts[matrix[x][y]]
    print(f" matrix_part: {matrix[x][y]}, part: {part}")
    next = None
    if part[0][0] != 0:
        if not (x+part[0][0] == prev_coordinates[0] and y == prev_coordinates[1]):
            next = (x+part[0][0], y)
    if part[0][1] != 0:
        if not (x+part[0][1] == prev_coordinates[0] and y == prev_coordinates[1]):
            next = (x+part[0][1], y)
    if part[1][0] != 0:
        if not (x == prev_coordinates[0] and y+part[1][0] == prev_coordinates[1]):
            next = (x, y+part[1][0])
    if part[1][1] != 0:
        if not (x == prev_coordinates[0] and y+part[1][1] == prev_coordinates[1]):
            next = (x, y+part[1][1])
    return next

def solve_puzzle(input):
    steps = 1
    with open(input, "r") as f:

        y = 0
        start_coordinates = None
        line = f.readline().rstrip()

        for i in range(len(line)):
            matrix.append([])

        while True:

            for i in range(len(line)):
                matrix[i].append(line[i])
            if "S" in line:
                start_coordinates = (line.index('S'), y)

            y += 1

            line = f.readline().rstrip()
            if not line:
                break

        print(matrix)

        active_coordinates = start_coordinates

        up_part = matrix[start_coordinates[0]][start_coordinates[1]-1]
        down_part = matrix[start_coordinates[0]][start_coordinates[1]+1]
        left_part = matrix[start_coordinates[0]-1][start_coordinates[1]]
        right_part = matrix[start_coordinates[0]+1][start_coordinates[1]]
        if parts[up_part][1][0] == -1:
            active_coordinates = (start_coordinates[0]-1, start_coordinates[1])
        elif parts[down_part][1][1] == 1:
            active_coordinates = (start_coordinates[0]+1, start_coordinates[1])
        elif parts[left_part][0][1] == 1:
            active_coordinates = (start_coordinates[0], start_coordinates[1]-1)
        elif parts[right_part][0][0] == -1:
            active_coordinates = (start_coordinates[0], start_coordinates[1]+1)
        prev_coordinates = start_coordinates

        while True:
            print(f" {prev_coordinates}    {active_coordinates}")
            next_coordinates = get_next_coordinates(prev_coordinates, active_coordinates)
            steps += 1
            if next_coordinates == start_coordinates:
                break
            prev_coordinates = active_coordinates
            active_coordinates = next_coordinates

    return steps/2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Filename containing puzzle input')
    args = parser.parse_args()

    result = solve_puzzle(args.input)
    print(result)

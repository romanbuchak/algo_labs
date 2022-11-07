from collections import defaultdict


def get_paths_number(corridor: list, height: int, width: int) -> int:
    solutions_in_line = [0] * height
    endpoints = set()
    squares_visited_count = defaultdict(int)

    for i in (0, height - 1):
        endpoint_square = corridor[i][width - 1]
        solutions_in_line[i] = 1
        endpoints.add(endpoint_square)
        squares_visited_count[endpoint_square] += 1

    for j in range(width - 2, -1, -1):
        current_column_paths_count = defaultdict(int)

        for i in range(height):
            square = corridor[i][j]
            if square not in endpoints and solutions_in_line[i] == 0:
                continue
            square_solution_count = squares_visited_count[square]

            if square is not corridor[i][j + 1]:
                square_solution_count += solutions_in_line[i]

            solutions_in_line[i] = square_solution_count
            current_column_paths_count[square] += square_solution_count

        for square_key in current_column_paths_count:
            endpoints.add(square_key)
            squares_visited_count[square_key] += current_column_paths_count[square_key]

    return sum(solutions_in_line)


def main(IN_FILE='ijones.in', OUT_FILE='ijones.out') -> None:
    with open(IN_FILE, 'r') as in_file:
        in_data = in_file.readlines()
    width, height = map(int, in_data[0].split(' '))
    corridor = [in_data[line].rstrip('\n') for line in range(1, height + 1)]
    paths_number = get_paths_number(corridor, height, width)

    open(OUT_FILE, 'w').write(str(paths_number))


if __name__ == '__main__':
    main()
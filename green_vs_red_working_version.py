import copy


def is_valid(pos, rows, cols):
    """This is a method that checks whether the cell coordinates are within the matrix"""

    row = pos[0]
    col = pos[1]
    return 0 <= row < rows and 0 <= col < cols


def get_neighbouring_green_cells_count(row, col, rows_num, columns_num, grid):
    """This is a method that returns the number of the green cells around"""

    nearby_green_cells = 0

    NEIGHBOURING_ROWS = [-1, -1, -1, 0, +1, +1, +1, 0]
    NEIGHBOURING_COLUMNS = [-1, 0, +1, +1, +1, 0, -1, -1]

    for i in range(8):
        current_position = [row + NEIGHBOURING_ROWS[i], col + NEIGHBOURING_COLUMNS[i]]
        if is_valid(current_position, rows_num, columns_num) and grid[current_position[0]][current_position[1]] == "1":
            nearby_green_cells += 1
    return nearby_green_cells


REQUIREMENT_RED_TO_GREEN = {3, 6}
REQUIREMENT_GREEN_TO_RED = {0, 1, 4, 5, 7, 8}

columns_number, rows_number = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows_number):
    matrix.append([x for x in input()])

cell_column, cell_row, turns = [int(x) for x in input().split(", ")]

turns_counter = 0
green_during_generations_count = 0
next_matrix = copy.deepcopy(matrix)

while True:
    if turns_counter == turns:
        if matrix[cell_row][cell_column] == "1":
            green_during_generations_count += 1
        break

    if matrix[cell_row][cell_column] == "1":
        green_during_generations_count += 1

    for row in range(rows_number):
        for column in range(columns_number):

            nearby_green_cells_count = get_neighbouring_green_cells_count(row, column, rows_number, columns_number,
                                                                          matrix)

            if matrix[row][column] == "0":
                if nearby_green_cells_count in REQUIREMENT_RED_TO_GREEN:
                    next_matrix[row][column] = "1"
            elif matrix[row][column] == "1":
                if nearby_green_cells_count in REQUIREMENT_GREEN_TO_RED:
                    next_matrix[row][column] = "0"

    matrix = copy.deepcopy(next_matrix)
    turns_counter += 1

print(green_during_generations_count)

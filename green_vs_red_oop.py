import copy

REQUIREMENT_RED_TO_GREEN = {3, 6}
REQUIREMENT_GREEN_TO_RED = {0, 1, 4, 5, 7, 8}


class Matrix:
    def __init__(self, input_line):
        self.matrix = []
        self.input_line = input_line
        self.columns_number, self.rows_number = [int(x) for x in input_line.split(", ")]

    def generate_matrix(self, *args):
        """This method generates the lines of the grid"""
        for i in range(self.rows_number):
            self.matrix.append([x for x in args[i]])

    def __repr__(self):
        return repr(self.matrix)


class Cell:
    """This class initializes the main cell object"""

    def __init__(self, input_line):
        self.input_line = input_line
        self.cell_column, self.cell_row, self.turns = [int(x) for x in input_line.split(", ")]


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


class Main:
    """This is a class where all the processing occurs"""

    def __init__(self, matrix, cell):
        self.matrix = matrix
        self.cell = cell

    def calculate_generations(self, matrix):
        """This method should return the number of generations in which the main cell has been green"""
        turns_counter = 0
        green_during_generations_count = 0
        next_matrix = copy.deepcopy(matrix)
        while True:
            if turns_counter == cell.turns:
                if matrix[cell.cell_row][cell.cell_column] == "1":
                    green_during_generations_count += 1
                break

            if matrix[cell.cell_row][cell.cell_column] == "1":
                green_during_generations_count += 1

            for row in range(matrix.rows_number):
                for column in range(matrix.columns_number):

                    nearby_green_cells_count = get_neighbouring_green_cells_count(row, column, matrix.rows_number, matrix.columns_number, matrix)

                    if matrix[row][column] == "0":
                        if nearby_green_cells_count in REQUIREMENT_RED_TO_GREEN:
                            next_matrix[row][column] = "1"
                    elif matrix[row][column] == "1":
                        if nearby_green_cells_count in REQUIREMENT_GREEN_TO_RED:
                            next_matrix[row][column] = "0"

            matrix = copy.deepcopy(next_matrix)
            turns_counter += 1
        return green_during_generations_count


matrix = Matrix("3, 3")
matrix.generate_matrix("000", "111", "000")
cell = Cell("1, 0, 10")
main = Main(matrix, cell)
main.calculate_generations(matrix)
print(green_during_generations_count)

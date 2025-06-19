import random

# initialise a 1D grid/array:
MAX_VALUE = 81
grid = [0] * MAX_VALUE

# this shifts the numbers starting from 1 along the row 
# and puts the elements at the end at the front
def shift(given_list, n):
    i = 0
    while i < n:
        given_list.insert(0, given_list.pop())
        i = i + 1
    return given_list

#print(shift(list(range(1, 10)), 3))

# filling in a 1D array for each row using the shift function
indices_to_shift = [0, 3, 6, 1, 4, 7, 2, 5, 8]
def fill_grid(grid):
    for i in range(0, len(grid), 9):
        initial_list = list(range(1, 10))
        grid[i:i+9] = shift(initial_list, indices_to_shift[int(i/9)])
    return grid

filled_grid = fill_grid(grid)
print(filled_grid)

# Function to just print the array as a sudoku grid
print("Printing the 1D array:")
print("---------------------------")
def print_grid(grid):
    for j in range(0, len(grid), 9):
        if j == 27 or j == 54 or j == 81: # to draw lines only
            print("---------------------------")
        part1 = grid[j:j+3]
        part1_to_s = ' '.join(map(str, part1))
        part2 = grid[j+3:j+6]
        part2_to_s = ' '.join(map(str, part2))
        part3= grid[j+6:j+9]
        part3_to_s = ' '.join(map(str, part3))
        print(" | " + part1_to_s + " | " + part2_to_s + " | " + part3_to_s + " | ")
    print("---------------------------")

print_grid(grid)

# given a grid and column to extract numbers from
def extract_column(grid, col_number):
    new_col = list()
    for i in range(col_number, len(grid), 9):
        new_col.append(grid[i])
    return new_col

#print(extract_column(oned_grid, 8))

# given a grid, column to move data to and column data
# replace the new column with the column data
def assign_columns(grid, col, col_data):
    for i in range(len(col_data)):
        grid[i*9 + col] = col_data[i]
    return grid

print("This is a grid with shuffled columns:")

def shuffle_columns(grid, col1, col2, col3):
    col_indices = [col1, col2, col3]
    col_dict = {col1: extract_column(grid, col1), 
                col2: extract_column(grid, col2), 
                col3: extract_column(grid, col3)}
    shuffled_indices = list(col_indices)
    random.shuffle(shuffled_indices)
    for i in range(len(col_indices)):
        col_index = col_indices[i]
        new_index = shuffled_indices[i]

        col_to_move = col_dict[col_index]
        assign_columns(grid, new_index, col_to_move)
    return grid

col1_shuffled = shuffle_columns(grid, 0, 1, 2)
col2_shuffled = shuffle_columns(grid, 3, 4, 5)
col3_shuffled = shuffle_columns(grid, 6, 7, 8)

print_grid(col3_shuffled)
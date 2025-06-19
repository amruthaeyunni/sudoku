import random
def sudokuGenerator(d, row):
    n = d * d # range of numbers to be printed so 3*3 = 9
    x = row # 1D array to print as 3x3 grid
    i = 0 # list index
    while i < n+1:
      print(" ".join(map(str, x[i:i+d]))) # choosing 3 numbers at a time, applying map function to convert them all to strings at the
                                          # same time and printing them on 1 line using spaces. 
      i += d # incrementing i by d again to choose next set of numbers
                
sudokuGenerator(3, list(range(1, 10)))

# initialising a 2D grid with only 0s
print("Generating an empty grid!")
def generate_grid(row, col):
    grid = [[0 for j in range(col)] for i in range(row)]
    return grid

grid = generate_grid(9, 9)
print(grid)
print("\n")

# Filling the initialised grid with random numbers from 1-9 for each row
print("Filling in the grid:")
def fill_grid(grid):
    for i in range(0, 9, 1):
        x = list(range(1, 10))
        random.shuffle(x)
        for j in range(0, 9, 1):
            #print(f"row: {i}, col: {j}, {grid[i]}, {grid[j]}")
            res = random.choice(x) # only choosing from the generated list to avoid repetition
            grid[i][j] = res
            x.remove(res)
    return grid

grid = fill_grid(grid)
print(grid)
print("\n")

# Formatting the output of the 2D array to visualise as a sudoku grid
print("Sudoku Grid:")
print("---------------------------")
def print_grid(grid):
    for i in range(0, len(grid), 3): # starts at 0th, 6th, and 9th rows
        # for each of the 3 rows
        row1 = grid[i]
        row2 = grid[i+1]
        row3 = grid[i+2]
        for j in range(0, len(row1), 3):
            # select the same 3 elements from each row at the same time and concatenate them
            sub_row1 = row1[j:j+3]
            row1_to_s = ' '.join(map(str, sub_row1))
            sub_row2 = row2[j:j+3]
            row2_to_s = ' '.join(map(str, sub_row2))
            sub_row3 = row3[j:j+3]
            row3_to_s = ' '.join(map(str, sub_row3))
            print(" | " + row1_to_s + " | " + row2_to_s + " | " + row3_to_s + " | ")
        print("---------------------------")
        
print_grid(grid)

print("Printing another grid")
def print_another_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0:
            print("---------------------------")
        j = 0
        part1 = grid[i][j:j+3]
        part1_to_s = ' '.join(map(str, part1))
        part2 = grid[i][j+3:j+6]
        part2_to_s = ' '.join(map(str, part2))
        part3= grid[i][j+6:j+9]
        part3_to_s = ' '.join(map(str, part3))
        print(" | " + part1_to_s + " | " + part2_to_s + " | " + part3_to_s + " | ")
    print("---------------------------")

print_another_grid(grid)

# initialise a 1D grid/array:
MAX_VALUE = 81
oned_grid = [0] * MAX_VALUE

def shift(given_list, n):
    i = 0
    while i < n:
        given_list.insert(0, given_list.pop())
        i = i + 1
    return given_list

print(shift(list(range(1, 10)), 3))


indices_to_shift = [0, 3, 6, 1, 4, 7, 2, 5, 8]
initial_list = list(range(1, 10))

def fill_grid2(oned_grid):
    for i in range(0, len(oned_grid), 9):
        initial_list = list(range(1, 10))
        oned_grid[i:i+9] = shift(initial_list, indices_to_shift[int(i/9)])
    return oned_grid

print(fill_grid2(oned_grid))

print("Printing the 1D array:")
print("---------------------------")
def print_new_grid(grid):
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

print_new_grid(oned_grid)

def extract_column(grid, col_number):
    new_col = list()
    for i in range(col_number, len(grid), 9):
        new_col.append(grid[i])
    return new_col

#print(extract_column(oned_grid, 8))

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

grid1 = shuffle_columns(oned_grid, 0, 1, 2)
grid3 = shuffle_columns(oned_grid, 3, 4, 5)
print_new_grid(grid1)
print_new_grid(grid3)
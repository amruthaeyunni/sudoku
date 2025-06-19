import random

class Sudoku:
    # Initialise a 1D grid/array:
    def __init__(self):
        self.max_value = 81
        self.grid = [0] * self.max_value

    # This shifts the numbers starting from 1 along the row 
    # and puts the elements at the end at the front
    def shift(given_list, n):
        i = 0
        while i < n:
            given_list.insert(0, given_list.pop())
            i = i + 1

        return given_list

    # Filling in a 1D array for each row using the shift function
    def fill_grid(grid, indices):
        indices_to_shift = indices

        for i in range(0, len(grid), 9):
            initial_list = list(range(1, 10))
            grid[i:i+9] = Sudoku.shift(initial_list, indices_to_shift[int(i/9)])

        return grid

    # Function to just print the array as a sudoku grid
    def print_grid(grid):
        print("---------------------------")

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

    # Given a grid and column number to extract elements from
    def extract_column(grid, col_number):
        new_col = list()

        for i in range(col_number, len(grid), 9):
            new_col.append(grid[i])

        return new_col

    # Given a grid, column to move data to and the column data
    # replace the new column with the column data
    def assign_columns(grid, col, col_data):
        for i in range(len(col_data)):
            grid[i*9 + col] = col_data[i]

        return grid

    def shuffle_columns(grid, col1, col2, col3):
        col_indices = [col1, col2, col3]

        # saving the original column data for each column before it gets changed
        # using a dictionary and key is the corresponding column number
        col_dict = {col1: Sudoku.extract_column(grid, col1), 
                    col2: Sudoku.extract_column(grid, col2), 
                    col3: Sudoku.extract_column(grid, col3)}
        
        shuffled_indices = list(col_indices) # making a copy of the original indices
        random.shuffle(shuffled_indices) # shuffling

        for i in range(len(col_indices)):
            col_index = col_indices[i] # original column index
            new_index = shuffled_indices[i] # new index to move column to

            col_to_move = col_dict[col_index] # retrieving the respective original column's data from dictionary
            Sudoku.assign_columns(grid, new_index, col_to_move) # moving to the new column
        return grid
    

def main():
    sudoku = Sudoku()

    indices_to_shift = [0, 3, 6, 1, 4, 7, 2, 5, 8]
    #print(shift(list(range(1, 10)), 3))
    filled_grid = Sudoku.fill_grid(sudoku.grid, indices_to_shift)
    print(filled_grid)

    print("Printing the 1D array:")
    Sudoku.print_grid(sudoku.grid)

    #print(extract_column(oned_grid, 8))

    # shuffling each column
    col1_shuffled = Sudoku.shuffle_columns(filled_grid, 0, 1, 2)
    col2_shuffled = Sudoku.shuffle_columns(col1_shuffled, 3, 4, 5)
    col3_shuffled = Sudoku.shuffle_columns(col2_shuffled, 6, 7, 8)
    
    print("This is a grid with the columns shuffled:")
    Sudoku.print_grid(col3_shuffled)

if __name__ == "__main__":
    main()
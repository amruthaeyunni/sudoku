import random

class Sudoku:
    # Initialise a 1D grid/array:
    def __init__(self):
        self.max_value = 81
        self.grid = [0] * self.max_value

    # This shifts the numbers starting from 1 along the row 
    # and puts the elements at the end at the front
    def shift(self, given_list, n):
        i = 0
        while i < n:
            given_list.insert(0, given_list.pop())
            i = i + 1

        return given_list

    # Filling in a 1D array for each row using the shift function
    def fill_grid(self, grid, indices):
        indices_to_shift = indices

        for i in range(0, len(grid), 9):
            initial_list = list(range(1, 10))
            grid[i:i+9] = self.shift(initial_list, indices_to_shift[int(i/9)])

        return grid

    # Function to just print the array as a sudoku grid
    def print_grid(self, grid):
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
    def extract_column(self, grid, col_number):
        new_col = list()

        for i in range(col_number, len(grid), 9):
            new_col.append(grid[i])

        return new_col

    # Given a grid, column to move data to and the column data
    # replace the new column with the column data
    def assign_columns(self, grid, col, col_data):
        for i in range(len(col_data)):
            grid[i*9 + col] = col_data[i]

        return grid

    def shuffle_columns(self, grid, col1, col2, col3):
        col_indices = [col1, col2, col3]

        # saving the original column data for each column before it gets changed
        # using a dictionary and key is the corresponding column number
        col_dict = {col1: self.extract_column(grid, col1), 
                    col2: self.extract_column(grid, col2), 
                    col3: self.extract_column(grid, col3)}
        
        shuffled_indices = list(col_indices) # making a copy of the original indices
        random.shuffle(shuffled_indices) # shuffling

        for i in range(len(col_indices)):
            col_index = col_indices[i] # original column index
            new_index = shuffled_indices[i] # new index to move column to

            col_to_move = col_dict[col_index] # retrieving the respective original column's data from dictionary
            self.assign_columns(grid, new_index, col_to_move) # moving to the new column

        return grid
    
    # Given a grid and row number to extract elements from
    def extract_row(self, grid, row_number):
        new_row = list()

        for i in range(row_number*9, row_number*9+9):
            new_row.append(grid[i])

        return new_row
    
    # Given a grid, row to move data to and the row data
    # replace the new row with the row data
    def assign_rows(self, grid, row, row_data):
        for i in range(9):
            grid[i+row*9] = row_data[i]
            #print(i+row*9)
        return grid
    
    # Given a grid, row to move data to and the row data
    # replace the new row with the row data
    def shuffle_rows(self, grid, row1, row2, row3):
        row_indices = [row1, row2, row3]

        # saving the original row data for each row before it gets changed
        # using a dictionary and key is the corresponding row number
        row_dict = {row1: self.extract_row(grid, row1), 
                    row2: self.extract_row(grid, row2), 
                    row3: self.extract_row(grid, row3)}

        shuffled_indices = list(row_indices) # making a copy of the original indices
        random.shuffle(shuffled_indices) # shuffling

        for i in range(len(row_indices)):
            row_index = row_indices[i] # original row index
            new_index = shuffled_indices[i] # new index to move row to

            row_to_move = row_dict[row_index] # retrieving the respective original row's data from dictionary
            self.assign_rows(grid, new_index, row_to_move) # moving to the new row

        return grid
    
    def shuffle(self, filled_grid):
        # shuffling each column
        col1_shuffled = self.shuffle_columns(filled_grid, 0, 1, 2)
        col2_shuffled = self.shuffle_columns(col1_shuffled, 3, 4, 5)
        col3_shuffled = self.shuffle_columns(col2_shuffled, 6, 7, 8)

        # shuffling each row
        row1_shuffled = self.shuffle_rows(col3_shuffled, 0, 1, 2)
        row2_shuffled = self.shuffle_rows(row1_shuffled, 3, 4, 5)
        row3_shuffled = self.shuffle_rows(row2_shuffled, 6, 7, 8)

        return row3_shuffled

    def remove_digits(self, grid, n):
        indices = random.sample(range(0, self.max_value), n)
        index_to_number = {}
        for i in range(len(indices)):
            index_to_number[indices[i]] = grid[indices[i]]
            #print(f"Index is: {indices[i]}, and grid number is: {grid[indices[i]]}")
        for j in range(len(grid)):
            if j in index_to_number.keys(): # if the grid index to remove is in the dictionary
                grid[j] = 0 # replace the value at that grid index with a 0
        return grid
    
    def is_valid(self, grid, num, index):
        row = index // 9 # retrieve the row of the number
        col = index % 9 # retrieve the column of the number

        # checking the row
        for i in range(9):
            index_in_row = row*9 + i
            # if the number at the current index already contains num and it is not the cell
            # currently being tested (inputted with num)
            if grid[index_in_row] == num and index_in_row != index:
                return False
        
        # checking the column
        for i in range(9):
            index_in_col = i*9 + col
            if grid[index_in_col] == num and index_in_col != index:
                return False
            
        # checking the box
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(3):
            for c in range(3):
                r_box = row_start + r
                c_box = col_start + c
                index_box = r_box * 9 + c_box

                if grid[index_box] == num and index_box != index:
                    return False
                
        return True # the number is not in the row, column or box so is valid at the current index

    # A method to find the next empty cell in the grid 
    def find_empty(self, grid):
        for i in range(len(grid)):
            if grid[i] == 0:
                return i # return the index of the empty cell
        return None # no empty cells so the grid is solved
    
    def solve_sudoku(self, grid):
        empty_cell = self.find_empty(grid) # first see if there are any empty cells
        if empty_cell is None:  # no empty cells found in the grid
            print("Grid has been solved!")
            self.print_grid(grid)
            return True # exit the method
        row = empty_cell // 9 # find the row of the empty cell
        col = empty_cell % 9 # find the column of the empty cell
        for i in range(1, 10): # test each number in the empty cell
            can_place_in_cell = self.is_valid(grid, i, empty_cell)
            print(f"Empty cell is: {empty_cell}, value at empty cell is: {grid[empty_cell]}")
            print(f"Row: [{row}], Col: [{col}], Value: {i}")
            print(f"Can place in cell?: {can_place_in_cell}")
            if can_place_in_cell:
                grid[empty_cell] = i
                print(f"Placing {i} in [{row}][{col}] at index {empty_cell}")
                self.print_grid(grid)
                res = self.solve_sudoku(grid) # check if the grid has been solved now
                if res:
                    return True
                else:
                    grid[empty_cell] = 0 # undo the change if the current number (i) can't be placed in this cell
                    print(f"Backtracking: Removed {i} from [{row}][{col}] at index {empty_cell}")
                    self.print_grid(grid)
        return False # no valid num found for this cell



def main():
    sudoku = Sudoku()

    indices_to_shift = [0, 3, 6, 1, 4, 7, 2, 5, 8]
    #print(shift(list(range(1, 10)), 3))
    filled_grid = sudoku.fill_grid(sudoku.grid, indices_to_shift)
    #print(filled_grid)

    print("Grid has been generated!")
    sudoku.print_grid(filled_grid)

    print("Grid has been shuffled!")
    shuffled_grid = sudoku.shuffle(filled_grid)
    sudoku.print_grid(shuffled_grid)

    print("Grid ready to solve!")
    puzzle = sudoku.remove_digits(shuffled_grid, 10)
    sudoku.print_grid(puzzle)

    print("Solving the grid!")
    solved = sudoku.solve_sudoku(puzzle)

    if not solved:
        print("Could not solve the grid")
        

if __name__ == "__main__":
    main()
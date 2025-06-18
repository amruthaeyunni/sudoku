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

# can generate a 2D grid of random numbers ranging from 1-9 - need to add checks
print("Generating the grid!")
def generate_grid(row, col):
    grid = [[0 for j in range(col)] for i in range(row)]
    return grid
#print(len(grid))
grid = generate_grid(9, 9)

print("Printing the 2D array:")
for i in range(0, 9, 1):
    x = list(range(1, 10))
    random.shuffle(x)
    for j in range(0, 9, 1):
        #print(f"row: {i}, col: {j}, {grid[i]}, {grid[j]}")
        res = random.choice(x)
        grid[i][j] = res
        x.remove(res)
print(grid)

print("Sudoku Grid:")
print("---------------------------")
def print_grid(grid):
    for i in range(0, len(grid), 3):
        row1 = grid[i]
        row2 = grid[i+1]
        row3 = grid[i+2]
        for j in range(0, len(row1), 3):
            sub_row1 = row1[j:j+3]
            row1_to_s = ' '.join(map(str, sub_row1))
            sub_row2 = row2[j:j+3]
            row2_to_s = ' '.join(map(str, sub_row2))
            sub_row3 = row3[j:j+3]
            row3_to_s = ' '.join(map(str, sub_row3))
            print(" | " + row1_to_s + " | " + row2_to_s + " | " + row3_to_s + " | ")
        print("---------------------------")
        
print_grid(grid)
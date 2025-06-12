import random
def sudokuGenerator(d):
    n = d * d # range of numbers to be printed so 3*3 = 9
    x = list(range(1, n+1)) # creates a list of the elements 1-9 inclusive
    print(x) 
    random.shuffle(x) # shuffling numbers to display grid differently everytime
    i = 0 # list index
    while i < n+1:
      print(" ".join(map(str, x[i:i+d]))) # choosing 3 numbers at a time, applying map function to convert them all to strings at the
                                          # same time and printing them on 1 line using spaces. 
      i += d # incrementing i by d again to choose next set of numbers
            
            
sudokuGenerator(3)

# can generate a 2D grid of random numbers ranging from 1-9 - need to add checks
row = 9
col = 9
grid = [[0 for j in range(col)] for i in range(row)]
#print(len(grid))

for i in range(0, 9, 1):
    x = list(range(1, 10))
    random.shuffle(x)
    for j in range(0, 9, 1):
        #print(f"row: {i}, col: {j}, {grid[i]}, {grid[j]}")
        res = random.choice(x)
        grid[i][j] = res
        x.remove(res)
print(grid)
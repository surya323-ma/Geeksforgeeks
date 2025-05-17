You are given a 2d array grid[][] of size n×n (where n = 2k and k≥1), with all cells initialized to 0 except for one missing cell. Your task is to fill the entire grid using L-shaped tiles. An L-shaped tile covers 3 cells in a 2x2 grid, with one cell missing. You need to tile the entire grid using the L-shaped tiles, ensuring that the missing cell remains untouched.

Note: The missing cell is denoted by "-1" and you should fill the rest of the grid with integers such that each group of three identical numbers corresponds to one L-shaped tile.
If you fill the entire grid correctly the driver code will print true else it will print false.

def can_fill_with_L_tiles(grid):
    n = len(grid)
    missing_cell = None
    
    # Find the position of the missing cell
    for i in range(n):
        for j in range(n):
            if grid[i][j] == -1:
                missing_cell = (i, j)
                break
        if missing_cell:
            break

    def place_tile(x, y, tile_number):
        # Place L-shaped tile if possible
        if (0 <= x < n and 0 <= y < n and grid[x][y] == 0):
            # Check all four orientations
            if (x + 1 < n and y + 1 < n and grid[x + 1][y] == 0 and grid[x][y + 1] == 0):
                # Place tile in orientation 1
                grid[x][y] = grid[x + 1][y] = grid[x][y + 1] = tile_number
                return True
            if (x + 1 < n and y - 1 >= 0 and grid[x + 1][y] == 0 and grid[x][y - 1] == 0):
                # Place tile in orientation 2
                grid[x][y] = grid[x + 1][y] = grid[x][y - 1] = tile_number
                return True
            if (x - 1 >= 0 and y + 1 < n and grid[x - 1][y] == 0 and grid[x][y + 1] == 0):
                # Place tile in orientation 3
                grid[x][y] = grid[x - 1][y] = grid[x][y + 1] = tile_number
                return True
            if (x - 1 >= 0 and y - 1 >= 0 and grid[x - 1][y] == 0 and grid[x][y - 1] == 0):
                # Place tile in orientation 4
                grid[x][y] = grid[x - 1][y] = grid[x][y - 1] = tile_number
                return True
        return False

    def remove_tile(x, y, tile_number):
        # Remove L-shaped tile
        if (0 <= x < n and 0 <= y < n and grid[x][y] == tile_number):
            grid[x][y] = 0

    def fill_grid(tile_number):
        # Check if the grid is completely filled
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) != missing_cell:
                    # Try to place a tile at (i, j)
                    if place_tile(i, j, tile_number):
                        # Recur to fill the rest
                        if fill_grid(tile_number + 1):
                            return True
                        # Backtrack
                        remove_tile(i, j, tile_number)
                    return False
        return True
    return fill_grid(1)

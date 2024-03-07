#!/usr/bin/python3
"""
Finding the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """calculates island perimeter"""
    if not isinstance(grid, list):
        return False

    # Check if each element of the list is also a list
    if not all(isinstance(inner_list, list) for inner_list in grid):
        return False

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check left neighbor
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right neighbor
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                # Check top neighbor
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter

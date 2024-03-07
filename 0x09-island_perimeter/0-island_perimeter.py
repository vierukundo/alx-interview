#!/usr/bin/python3
"""
Finding the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    # Check if parameter is a list
    if not isinstance(grid, list):
        return False

    # Check if each element of the list is also a list
    if not all(isinstance(inner_list, list) for inner_list in grid):
        return False

    # Check if each element of the inner lists is an integer
    if not all(isinstance(element, int) for inner_list in grid for element in inner_list):
        return False

    done = False
    cells = 0
    previous_cell = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if previous_cell == []:
                    previous_cell = [i, j]
                    cells += 1
                elif i or j in previous_cell:
                    previous_cell = [i, j]
                    cells += 1
                else:
                    done = True
                    break
        if done:
            break
    perimeter = (cells * 2) + 2
    return perimeter

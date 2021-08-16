# Starting in the top left corner of a 2x2 grid, and only being able
# to move to the right and down, there are exactlt 6 routes to the bottom
# right corner

# How many such routes are there through a 20x20 grid?
#==========================================================================#
from pprint import pprint

grid_points = 21 # The number of points
grid = [[num for num in range(grid_points)] for _ in range(grid_points)]    # We need the coordinates
                                                                            # of the points not the squares

grid = [[0 for _ in range(grid_points)] for _ in range(grid_points)]  # We need the coordinates

# From the end upward

def right(loc):
    if loc['x'] < grid_points - 1:
        return True
    return False

def below(loc):
    if loc['y'] < grid_points - 1:
        return True
    return False

def right_cell(loc):
    x = loc['x'] + 1 # the column to the right
    y = loc['y'] 
    value = grid[y][x]
    return value

def cell_below(loc):
    x = loc['x']
    y = loc['y'] + 1 # the row below
    value = grid[y][x]
    return value

def edge(loc):
    if loc['x'] == len(grid[y])-1:return True
    if loc['y'] == len(grid)-1:return True
    return False

curr_loc = {'x': 0, 'y': 0}
y = len(grid) - 1
while y >= 0:
    x = len(grid[y]) - 1
    while x >= 0:
        curr_loc['x'] = x
        curr_loc['y'] = y
#        print ('location: {}'.format(curr_loc))
#        print ('the value at location is {}'.format(grid[y][x]))
        if not edge(curr_loc):

            if right(curr_loc):
#                print ('Is there a cell right? {} value of the cell is {}'.format(right(curr_loc), right_cell(curr_loc)))
                grid[y][x] += right_cell(curr_loc)

            if below(curr_loc):
#                print ('Is there a cell below? {} value of the cell is {}'.format(below(curr_loc), cell_below(curr_loc)))
#                print (curr_loc['y'] + 1, curr_loc['x'])
                grid[y][x] += cell_below(curr_loc)
        
        else: grid[y][x] = 1

#        print('new value at current location is {}'.format(grid[y][x]))
        x -= 1
    y -= 1

print (grid[0][0])


















'''
#IDEA: just parse through it... deffinetly not the best solution
paths = 0
# Okay, Essentially there is something fundamentally wrong with this way of searching the value
# Am I covering paths multiple times ? - well not really, but the assigned values don't correspond
# to the actual ones. It's just a wrong way of counting the paths
for y in range(len(grid)):
    for x in range(len(grid[y])):
        curr_loc = (x, y)
        goal = (max(grid[y]), len(grid) - 1)
        # print ('max row value: {}'.format(max(grid[y])))
        # print ('len grid value: {}'.format(len(grid) - 1))
        if curr_loc == goal: paths += 0
        elif curr_loc[0] == max(grid[y]) or curr_loc[1] == len(grid) - 1:
            # print ('points = 1 : {}'.format(curr_loc))
            paths += 1
        else:
            # print ('points = 2 : {}'.format(curr_loc))
            paths += 2
print (paths)
'''














#===================== Okay, wrong Logic I guess :/ =====================#
# IDEA: count the corners with one and 2 options. Then divide the sum by 2
# Works for 1x1, 2x2 and 3x3.
# The amount is 20*20 + 20*2 = 440 -> 220 paths

'''
curr_loc = [0, 0]
count_doubles = 0 # count the points from, which you have two ways
count_singles = 0 # count the points from, which you have only one way
for row in grid:
    goal = [row.index(row[-1]), grid.index(grid[-1])]
    for el in row:
        curr_loc[0] = row.index(el)
        curr_loc[1] = grid.index(row)
        if curr_loc[0] == goal[0] and curr_loc[1] == goal[1]:break              # don't count the bottom right corner
        elif curr_loc[0] == goal[0] or curr_loc[1] == goal[1]:count_singles +=1 # If the we are on the edge 
        else:count_doubles +=1

print (count_singles)
print (count_doubles)
paths_to_corner = (1 * count_singles + count_doubles * 2)/2 # Always an even/2

print (paths_to_corner)
'''

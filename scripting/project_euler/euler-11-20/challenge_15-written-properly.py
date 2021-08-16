# Algorithmnic Solution
def CalculateNumberOfPaths(gridSize):

    paths = [[0 for i in range(gridSize + 1)] for i in range(gridSize + 1)]
    paths[gridSize][gridSize] = 1
    queue = [(gridSize, gridSize)]

    while queue:
        current = queue.pop(0)

        if current[0] - 1 >= 0: # check to left
            if (current[0] - 1, current[1]) not in queue:
                queue.append((current[0] - 1, current[1]))
            paths[current[0] - 1][current[1]] += paths[current[0]][current[1]]

        if current[1] - 1 >= 0: # check above
            if (current[0], current[1] - 1) not in queue:
                queue.append((current[0], current[1] - 1))
            paths[current[0]][current[1] - 1] += paths[current[0]][current[1]]
       
    return paths[0][0]

print(CalculateNumberOfPaths(20))

# Combinatorical Solution

# Denominate a path as RRDD -> right, right, down, down
# Now we need to calculate all permutations of R and D
# such that there are n Rs and n Ds, where n is the grid size

# Another way we could ask the question is:
# In how many ways can we pick k Rs from n available positions
# where k = n/2?
# Essentially, we calculate binomial coefficient (n/k)

# Note that starting Python 3.8, the standard library provides the math.comb function to compute the binomial coefficient:

# math.comb(n, k)

# which is the number of ways to choose k items from n items without repetition
# n! / (k! (n - k)!):

import math
gridSize = 20
combSlots = gridSize * 2
print(math.comb(combSlots, gridSize))

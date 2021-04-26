# Python3 program for the calculation of largest number of connected blocks

# Keeps a track of directions
# that is up, down, left, right
dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

# Function to perform the dfs traversal
def dfs(a, b, lis, x, y):

    global id, length, diameter

    # Mark the current node as visited
    vis[a][b] = id

    # Increment length from this node
    length += 1

    # Update the diameter length
    if (length > diameter):
        x = a
        y = b
        diameter = length

    for j in range(4):

        # Move to next cell in x-direction
        cx = a + dx[j]

        # Move to next cell in y-direction
        cy = b + dy[j]

        # Check if cell is invalid
        # then continue
        if (cx < 0 or cy < 0 or
            cx >= row or cy >= col or
            lis[cx][cy] == 0 or vis[cx][cy]):
            continue

        # Perform DFS on new cell
        dfs(cx, cy, lis, x, y)

    vis[a][b] = 0

    # Decrement the length
    length -= 1

    return x, y

# Function to find the maximum length of
# connected 1s in the given grid
def findMaximumLength(lis):

    global id, length, diameter

    x = 0
    y = 0

    # Increment the id
    id += 1

    length = 0
    diameter = 0

    # Traverse the grid[]
    for i in range(row):
        for j in range(col):
            if (lis[i][j] != 0):

                # Find start point of
                # start dfs call
                x, y = dfs(i, j, lis, x, y)
                i = row
                break

    id += 1
    length = 0
    diameter = 0

    # DFS Traversal from cell (x, y)
    x, y = dfs(x, y, lis, x, y)

    # Print the maximum length
    print(diameter)


    # Given grid[][]
row = int(input('Enter the number of rows : '))

col = int(input('Enter the number of columns: '))

print('Enter the grid cell values: ')

vis = [[0 for i in range(col + 1)]
        for j in range(row + 1)]
id = 0
diameter = 0
length = 0


grid = []

for _ in range(row):
    grid.append(list(map(int,input().rstrip().split())))
findMaximumLength(grid)

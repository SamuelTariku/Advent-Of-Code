
class Grid:
    def __init__(self, grid_str: list[list[str]]):

        if len(grid_str) == 0:
            raise Exception("Empty Grid")
        self.height = len(grid_str)
        self.width = len(grid_str[0])

        for rows in grid_str:
            if len(rows) != self.width:
                raise Exception("Uneven width sizes")

        self.grid = grid_str
        self.beams = []

        # Find and assign initial beam
        for i in range(len(grid_str)):
            for j in range(len(grid_str[i])):
                if grid_str[i][j] == "S" and grid_str[i][j+1] == ".":
                    grid_str[i+1][j] = "|"
                    self.beams.append((i+1, j))

    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value
        else:
            IndexError("Coordniates Out of grid")

    def addBeam(self, x, y):
        self.set(x, y, "|")
        self.beams.append((y, x))

    def get(self, x, y):
        return self.grid[y][x]

    def __repr__(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(grid[i][j], end="")
            print()

# def checkPoint(grid: list[list[str]], x: int, y: int) -> tuple | None:
#     try:
#         return grid[y][x]
#     except IndexError:
#         return None


with open("./test.txt", "r", encoding="utf8") as file:
    grid = Grid([list(i) for i in file.read().splitlines()])

# # Find starting point and add initial beam
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S" and grid[i][j+1] == ".":
            grid[i+1][j] = "|"
            beams.append((i+1, j))

i = 0
while True:
    print(f"iter: {i}")
    if i >= len(grid.beams):
        break

    # infinite loop break
    if i > 20:
        print("infinite loop break")
        break

    # Try to get the next bottom point
    # If it cant get it then its at the bottom
    nextPointX = beams[i][1]
    nextPointY = beams[i][0]+1
    nextPointChar = checkPoint(grid, nextPointX, nextPointY)

    if nextPointChar is None:
        i += 1
        continue

    if nextPointChar == ".":
        beams.append((nextPointY, nextPointX))
        grid[nextPointY][nextPointX] = "|"

    elif nextPointChar == "^":
        leftPoint = (nextPointY, nextPointX - 1)
        if checkPoint(grid, leftPoint[0], leftPoint[1]) == ".":
            beams.append(leftPoint)
            grid[leftPoint[0]][leftPoint[1]] = "|"

        rightPoint = (nextPointX + 1, nextPointY)
        if checkPoint(grid, rightPoint[0], rightPoint[1]) == ".":
            beams.append(rightPoint)
            grid[rightPoint[0]][rightPoint[1]] = "|"
    i += 1



print(f"beams: {beams}")

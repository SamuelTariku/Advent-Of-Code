
class GridObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        if not self.is_in_bounds(x, y):
            return "OUT_OF_BOUNDS"
        return self.grid[y][x]

    def instantiate(self, obj: GridObject):
        self.grid[obj.y][obj.x] = obj

    def parse_str(self, input_grid: str):
        startingPoints = []
        for i in range(len(input_grid)):
            for j in range(len(input_grid[i])):
                if input_grid[i][j] == "S":
                    start = StartPoint(j, i)
                    self.grid[i][j] = start
                    startingPoints.append(start)

                elif input_grid[i][j] == "^":
                    self.grid[i][j] = Splitter(j, i)
        return startingPoints

    def print(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is None:
                    print(".", end="")
                else:
                    print(self.grid[i][j], end="")
            print()


class StartPoint(GridObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "S"

    def start(self, grid):
        target_tile = grid.get(self.x, self.y + 1)

        if target_tile == "OUT_OF_BOUNDS":
            return

        if isinstance(target_tile, Beam):
            return

        if isinstance(target_tile, Splitter):
            target_tile.split()
            return

        if target_tile is None:
            grid.instantiate(Beam(self.x, self.y + 1, grid))
            return


class Splitter(GridObject):

    splits = 0

    def __init__(self, x, y):
        super().__init__(x, y)
        self.has_split = False

    def __repr__(self):
        return "^"

    def split_offset(self, grid, x_offset):
        target_tile = grid.get(self.x + x_offset, self.y)

        if target_tile == "OUT_OF_BOUNDS":
            return
        if isinstance(target_tile, Beam):
            return
        if isinstance(target_tile, Splitter):
            if not target_tile.has_split:
                target_tile.split(grid)
            return
        if target_tile is None:
            grid.instantiate(Beam(self.x + x_offset, self.y, grid))
            return

    def split(self, grid):
        self.split_offset(grid, -1)
        self.split_offset(grid, 1)
        self.has_split = True
        # print(f"splitting at {self.x, self.y}")
        Splitter.splits += 1


class Beam(GridObject):
    def __init__(self, x, y, grid):
        super().__init__(x, y)
        # check tile below
        target_tile = grid.get(self.x, self.y + 1)

        if target_tile == "OUT_OF_BOUNDS":
            return

        if isinstance(target_tile, Beam):
            return

        if isinstance(target_tile, Splitter):
            target_tile.split(grid)
            return

        if target_tile is None:
            grid.instantiate(Beam(self.x, self.y + 1, grid))
            return

    def __repr__(self):
        return "|"


def main():
    with open("./input.txt", "r", encoding="utf8") as file:
        input_grid = [list(i) for i in file.read().splitlines()]

    if len(input_grid) == 0:
        print("Error: Empty Grid")
        return

    height = len(input_grid)
    width = len(input_grid[0])
    for i in range(len(input_grid)):
        if len(input_grid[i]) != width:
            print(f"Inconsistent columns at y={i}")

    grid = Grid(width, height)
    startingPoints = grid.parse_str(input_grid)

    print([(s.x, s.y) for s in startingPoints])
    for s in startingPoints:
        s.start(grid)

    grid.print()
    print(Splitter.splits)
    


if __name__ == "__main__":
    main()

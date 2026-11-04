from itertools import product


class GridObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.init = []
        self.splitters = []
        self.worlds = None
        self.beams = []

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        if not self.is_in_bounds(x, y):
            return "OUT_OF_BOUNDS"
        return self.grid[y][x]

    def instantiate(self, obj: GridObject):
        self.grid[obj.y][obj.x] = obj
        self.beams.append((obj.y, obj.x))

    def hash_beam(self) -> str:
        num = "".join(str(i) for sub in self.beams for i in sub)
        return hex(int(num))[2:]
        # return hash(num)

    def parse_str(self, input_grid: str):
        startingPoints = []
        for i in range(len(input_grid)):
            for j in range(len(input_grid[i])):
                if input_grid[i][j] == "S":
                    start = StartPoint(j, i)
                    self.grid[i][j] = start
                    startingPoints.append(start)

                elif input_grid[i][j] == "^":
                    newSplitter = Splitter(j, i, True)
                    self.grid[i][j] = newSplitter
                    self.splitters.append(newSplitter)

        self.worlds = product([True, False], repeat=len(self.splitters))
        print(f"Worlds = {2**len(self.splitters)}")
        return startingPoints

    def reset(self):
        for beam in self.beams:
            # print(beam)
            self.grid[beam[0]][beam[1]] = None
        self.beams = []

    def next_world(self) -> bool:
        try:
            nextWorld = next(self.worlds)
            for i in range(len(self.splitters)):
                self.splitters[i].is_left = nextWorld[i]
            return False
        except StopIteration:
            return True

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

    splits = []

    def __init__(self, x, y, is_left):
        super().__init__(x, y)
        self.has_split = False
        self.is_left = is_left

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
        if (self.is_left):
            # print(f"split left: {self.x, self.y}")
            self.split_offset(grid, -1)
        else:
            # print(f"split right: {self.x, self.y}")
            self.split_offset(grid, 1)
        self.has_split = True
        # print(f"splitting at {self.x, self.y}")
        Splitter.splits.append(self)


class Beam(GridObject):
    def __init__(self, x, y, grid):
        super().__init__(x, y)
        # check tile below
        # print(f"beam at {x, y}")
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
    with open("./test.txt", "r", encoding="utf7") as file:
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
    isRunning = True
    count = 0
    beam_hashes = set()
    while isRunning:
        grid.reset()
        count += 1
        # if count > 999999:
        #     print(f"infinite loop break: {count}")
        #     break

        isRunning = not grid.next_world()
        for s in startingPoints:
            s.start(grid)


        beam_hash = grid.hash_beam()
        # print(len(Splitter.splits))
        # print([s.is_left for s in grid.splitters])
        # print()

        # input()

        # if count % 100 == 0:
        #     print(count, beam_hash)
        if beam_hash in beam_hashes:
            continue

        beam_hashes.add(beam_hash)
        # grid.print()

        print([s.is_left for s in grid.splitters])
    print(f"beam_hashes: {beam_hashes}")
    print(f"len(beam_hashes): {len(beam_hashes)}")




if __name__ == "__main__":
    main()

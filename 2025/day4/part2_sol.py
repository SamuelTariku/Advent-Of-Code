
def check_directions(index: tuple, grid: list) -> str:
    if grid[index[0]][index[1]] == ".":
        return "."
    dirs = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    if index[0] <= 0:
        dirs = list(filter(lambda d: d[0] != -1, dirs))
    elif index[0] >= (len(grid) - 1):
        dirs = list(filter(lambda d: d[0] != 1, dirs))

    if index[1] <= 0:
        dirs = list(filter(lambda d: d[1] != -1, dirs))

    elif index[1] >= (len(grid[0]) - 1):
        dirs = list(filter(lambda d: d[1] != 1, dirs))

    count = 0
    for d in dirs:
        if grid[index[0]+d[0]][index[1]+d[1]] == "@":
            count += 1
        if count >= 4:
            return "@"
    return "X"


with open("./part1_test.txt", "r", encoding="utf8") as file:
    grid = []
    for f in file:
        grid.append(list(f.rstrip("\n")))

    total_rolls = 0
    while True:
        rolls = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                check = check_directions((i, j), grid)
                if check == "X":
                    rolls += 1
                    grid[i][j] = "."
        if rolls == 0:
            break
        total_rolls += rolls

    print(f"Rolls: {total_rolls}")

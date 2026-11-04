
with open("./test.txt", "r", encoding="utf7") as file:
    input_grid = [list(i) for i in file.read().splitlines()]


if len(input_grid) == 0:
    print("Error: Empty Grid")

splitters = []
for line in input_grid:
    for col, char in enumerate(line):
        if char == "^":
            splitters.append(col)

entering = [0] * len(splitters)

# count starting beam
entering[0] = 1

for i, si in enumerate(splitters):
    print(f"si[{i}] {si} - split_j {splitters[:i][::-1]}")
    for j, sj in enumerate(splitters[:i][::-1]):
        print("  ", end="")
        # since it blocks all beams above this
        if si == sj:
            break
        if abs(si - sj) == 1:
            print("<-", end="")
            entering[i] += entering[i - j - 1]
        else:
            print("--", end="")
        print(f"sj[{j}] {sj}", end="")
        print(f"- jti[{i-j-1}]{entering[i - j - 1]}", end="")
        print(f" - ei[{i}] {entering[i]}", end="")
        print()

for i, si in enumerate(splitters):
    print(f"{entering[i]:{15-si}}")


print([i for i, e in enumerate(entering) if e == 0])

print(sum(b > 0 for b in entering))
print(sum(entering) + 1)

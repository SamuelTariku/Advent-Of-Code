# Not using range() since this way is the fastest method
def check_range(value, lower, upper) -> bool:
    if lower <= value <= upper:
        return True
    return False


with open("./part1_input.txt", "r", encoding="utf8") as file:
    ranges = []
    total = 0
    for f in file:
        line = f.rstrip("\n")
        if line == "":
            break

        rangeVal = [int(i) for i in line.split("-")]
        ranges.append((rangeVal[0], rangeVal[1]))

    newRanges = []
    ranges.sort()
    skips = []
    for i in range(len(ranges)):
        lower, upper = ranges[i]
        if i in skips:
            continue
        for j in range(i+1, len(ranges)):
            if upper >= ranges[j][0]:
                print(f"*i: {lower, upper} j:{ranges[j]}")
                upper = ranges[j][1]
                skips.append(j)
            else:
                print(f"i: {lower, upper} j:{ranges[j]}")
        newRanges.append((lower, upper))
    print(newRanges)

    total = 0
    for r in newRanges:
        total += r[1]+1 - r[0]

    print()
    print(f"skips: {len(skips)}")
    print(f"Total: {total}")

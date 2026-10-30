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
    for i in range(len(ranges)):
        start, end = ranges[i]
        if not newRanges or newRanges[-1][1] < start - 1:
            # print(f"i: {start, end} i:{ranges[i]}")
            newRanges.append([start, end])
        else:
            # print(f"*i: {start, end} i:{ranges[i]}")
            newRanges[-1][1] = max(end, newRanges[-1][1])

    # print(newRanges)

    total = 0
    for r in newRanges:
        total += r[1]+1 - r[0]

    print()
    print(len(newRanges))
    print(f"Total: {total}")

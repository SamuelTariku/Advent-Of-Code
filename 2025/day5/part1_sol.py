
# Not using range() since this way is the fastest method
def check_range(value, lower, upper) -> bool:
    if lower <= value <= upper:
        return True
    return False


with open("./part1_input.txt", "r", encoding="utf8") as file:
    ranges = []
    availableIDs = []
    isIngredients = False
    for f in file:
        line = f.rstrip("\n")
        if line == "":
            isIngredients = True
            continue
        if isIngredients:
            availableIDs.append(int(line))
            continue

        rangeVal = [int(i) for i in line.split("-")]
        ranges.append((rangeVal[0], rangeVal[1]))

    count = 0
    for i in availableIDs:
        for r in ranges:
            if check_range(i, r[0], r[1]):
                count += 1
                break

    print(ranges)
    print(availableIDs)
    print(f"Count: {count}")

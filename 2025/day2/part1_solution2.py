from typing import List

# We are looking for symmetric numbers
with open("test.txt", "r") as f:
    content = f.read()
    ranges = content.replace("\n", "").split(",")

    # Get all IDs
    ids: List[int] = []
    for r in ranges:
        rangeNums = r.split("-")
        if (len(rangeNums) < 2 or len(rangeNums) > 2):
            print(f"invalid range added: {r}")
            continue
        try:
            r0 = int(rangeNums[0])
            r1 = int(rangeNums[1])
            ids += [i for i in range(r0, r1+1)]
        except ValueError:
            print(f"invalid range type: {r}")
            continue

    # Check Ids for invalid values
    invalidIds = []
    for i in ids:
        strNum = str(i)
        if ((len(strNum) % 2) != 0):
            continue
        halfLen = len(strNum) // 2
        if (strNum[:halfLen] == strNum[halfLen:]):
            invalidIds.append(i)
    print(invalidIds)
    print(sum(invalidIds))

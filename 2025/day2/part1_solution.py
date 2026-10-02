# We are looking for symmetric numbers
with open("input.txt", "r") as f:
    content = f.read()
    ranges = content.replace("\n", "").split(",")
    invalidIds = []
    for r in ranges:
        rangeNums = r.split("-")
        if (len(rangeNums) < 2 or len(rangeNums) > 2):
            print(f"invalid range added: {r}")
            continue
        r1int = 0
        r2int = 0
        try:
            r1int = int(rangeNums[0])
            r2int = int(rangeNums[1])
        except ValueError:
            print(f"invalid range type: {r}")
            continue

        for i in range(r1int, r2int+1):
            strNum = str(i)
            if ((len(strNum) % 2) != 0):
                continue
            halfLen = len(strNum) // 2
            if (strNum[:halfLen] == strNum[halfLen:]):
                invalidIds.append(i)
    print(invalidIds)
    print(sum(invalidIds))

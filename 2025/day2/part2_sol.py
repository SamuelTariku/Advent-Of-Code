
def CheckIfInvalid(ids):
    invalidIds = []
    for i in range(0, len(ids)):
        percent = (i / len(ids) * 100)
        print(round(percent, 2), f"{i}/{len(ids)}")
        strNum = str(ids[i])
        for j in reversed(range(2, len(strNum)+1)):
            # print("j", j, "len(strNum)", len(strNum))
            if ((len(strNum) % j) != 0):
                continue
            cutLen = len(strNum) // j
            compareStr = strNum[:cutLen]
            # print("comparing", compareStr, "in", strNum, "cutLen", cutLen)
            is_mismatch = False
            for k in range(2, j+1):
                # print("cutIndexRange", cutLen*(k-1), "-", cutLen*k, "cutSection", strNum[(cutLen*(k-1)):(cutLen*k)])
                if (strNum[cutLen*(k-1):cutLen*k] != compareStr):
                    # print("mismatch between", strNum[cutLen*k-1:cutLen*k], "and", compareStr)
                    is_mismatch = True
                    break
            if (not is_mismatch):
                # print("invalid id: ", i, "for j", j)
                invalidIds.append(ids[i])
                break
    return invalidIds


# We are looking for symmetric numbers
def main():
    with open("./part1_input.txt", "r") as f:
        content = f.read()
        ranges = content.replace("\n", "").split(",")

        # Get all IDs
        ids = []
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

        invalidIds = CheckIfInvalid(ids)
        # Check Ids for invalid values
        print("ids", invalidIds)
        print("sum", sum(invalidIds))


if __name__ == "__main__":
    main()

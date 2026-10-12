

def highlightRed(text):
    return "\033[31m" + text + "\033[0m"


def highlightBlue(text):
    return "\033[44m" + text + "\033[0m"


def getWithhighlightRed(line, indexJoltList, maxj, start, end):
    newLine = ""
    for k in range(0, len(line.rstrip('\n'))):
        if (k == start):
            newLine += "["
        if (k == end + 1):
            newLine += "]"
        if (k == maxj):
            newLine += highlightBlue(line[k])
            continue
        if (k in indexJoltList):
            newLine += highlightRed(line[k])
            continue
        newLine += line[k]
    return newLine


def checkOrderedMax(line, lineInt):
    lineIndex = [i for i in range(0, len(lineInt))]
    indexJoltList = []
    start = 0
    end = len(lineInt)
    rev = False
    while True:

        if len(indexJoltList) == 12:
            break

        if start >= end:
            remaining = []
            # minIndex = min(indexJoltList)
            for i in reversed(lineIndex):
                if i in indexJoltList:
                    # print(f"I is {i}, listIndex is {lineIndex}")
                    lineIndex.pop(lineIndex.index(i))
                else:
                    remaining.append(i)

            minIndex = 0
            # break into multiple sections
            for j in reversed(indexJoltList):
                found = False
                for i in lineIndex:
                    if i > j:
                        # translate to lineIndex
                        minIndex = lineIndex.index(i)
                        found = True
                        # print(f"found lineIndex:{i} indexJoltList:{
                        #       j}, minIndex:{minIndex}")
                        break
                if found:
                    break

            start = minIndex
            end = len(lineIndex)
            # print(f"section: {lineIndex[start:end]}")

            # print(f"remaining: {getWithhighlightRed(
            # line, remaining)}, new lineIndex: {lineIndex}")

        # Chcek list for max values
        if rev:
            maxj = end - 1
            iter = reversed(range(start, end))
        else:
            maxj = start
            iter = range(start, end)

        for j in iter:
            if lineInt[lineIndex[j]] > lineInt[lineIndex[maxj]]:
                maxj = j

        if maxj == (end - 1):
            print(f"-> s:{start} e:{end}, maxval:{
                lineInt[lineIndex[maxj]]} jolt:{
                getWithhighlightRed(line, indexJoltList, maxj, start, end)}")
            indexJoltList.append(lineIndex[maxj])
            end = maxj
            continue
        print(f"<- s:{start} e:{end}, maxval:{
            lineInt[lineIndex[maxj]]} jolt:{
            getWithhighlightRed(line, indexJoltList, maxj, start, end)}")
        indexJoltList.append(lineIndex[maxj])
        start = maxj + 1

    return indexJoltList


def main():
    with open("./part1_input.txt", "r", encoding="utf8") as file:
        joltages = []
        for line in file:
            lineInt = [int(i) for i in list(line.rstrip("\n"))]

            indexJoltList = checkOrderedMax(line, lineInt)

            print("jolti:", indexJoltList, "joltLen:", len(indexJoltList))
            print()

            print("HighLight View:", getWithhighlightRed(line, indexJoltList, None, 0, len(line)))
            finalJoltString = ""
            for k in range(0, len(line.rstrip('\n'))):
                if (k in indexJoltList):
                    finalJoltString += line[k]
                    continue
            print("finalJoltString: ", finalJoltString)
            joltages.append(int(finalJoltString))

        print("\n\njolts", joltages)
        print("sum", sum(joltages))


if __name__ == "__main__":
    main()

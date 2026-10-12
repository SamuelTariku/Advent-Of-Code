

def underline(text):
    return "\033[31m" + text + "\033[0m"


def getWithHighlight(line, indexJoltList):
    newLine = ""
    for k in range(0, len(line.rstrip('\n'))):
        if (k in indexJoltList):
            newLine += underline(line[k])
            continue
        newLine += line[k]
    return newLine


def checkOrderedMax(line, lineInt):
    lineIndex = [i for i in range(0, len(lineInt))]
    indexJoltList = []
    start = 0
    end = len(lineInt)
    print("lineInt", lineInt)
    while True:

        if len(indexJoltList) == 12:
            break
        #
        # if start >= end:
        #     remaining = []
        #     for i in reversed(range(0, len(lineInt))):
        #         if i not in indexJoltList:
        #             indexJoltList.append(i)
        #             remaining.append(i)
        #
        #         if len(indexJoltList) == 12:
        #             break
        #     print(f"remaining: {getWithHighlight(line, remaining)}")
        #     break
        #
        if start >= end:
            remaining = []
            minIndex = min(indexJoltList)
            for i in reversed(lineIndex):
                if i in indexJoltList:
                    lineIndex.pop(i)
                else:
                    remaining.append(i)

            start = 0
            end = len(lineIndex)

            print(f"remaining: {getWithHighlight(
                line, remaining)}, new lineIndex: {lineIndex}")

        maxj = start
        for j in range(start, end):
            if lineInt[lineIndex[j]] > lineInt[lineIndex[maxj]]:
                maxj = j
        if maxj == (end - 1):
            print(f"-> s:{start} e:{end}, maxj:{maxj} val:{lineInt[lineIndex[maxj]]} lineIndex:{
                  lineIndex} jolt:{getWithHighlight(line, indexJoltList)}")
            indexJoltList.append(lineIndex[maxj])
            end = maxj
            continue

        print(f"<- s:{start} e:{end}, maxj:{maxj} val:{lineInt[lineIndex[maxj]]} lineIndex:{
              lineIndex} jolt:{getWithHighlight(line, indexJoltList)}")
        indexJoltList.append(lineIndex[maxj])
        start = maxj + 1

    return indexJoltList


def main():
    with open("./part1_test.txt", "r", encoding="utf8") as file:
        joltages = []
        for line in file:
            lineInt = [int(i) for i in list(line.rstrip("\n"))]

            lineIndex = [i for i in range(0, len(lineInt))]
            indexJoltList = []
            start = 0
            end = len(lineInt)
            print("lineInt", lineInt)
            while True:

                if len(indexJoltList) == 12:
                    break
                #
                # if start >= end:
                #     remaining = []
                #     for i in reversed(range(0, len(lineInt))):
                #         if i not in indexJoltList:
                #             indexJoltList.append(i)
                #             remaining.append(i)
                #
                #         if len(indexJoltList) == 12:
                #             break
                #     print(f"remaining: {getWithHighlight(line, remaining)}")
                #     break
                #
                if start >= end:
                    remaining = []
                    minIndex = min(indexJoltList)
                    for i in reversed(lineIndex):
                        if i in indexJoltList:
                            lineIndex.pop(i)
                        else:
                            remaining.append(i)

                    start = 0
                    end = len(lineIndex)

                    print(f"remaining: {getWithHighlight(
                        line, remaining)}, new lineIndex: {lineIndex}")

                maxj = start
                for j in range(start, end):
                    if lineInt[lineIndex[j]] > lineInt[lineIndex[maxj]]:
                        maxj = j
                if maxj == (end - 1):
                    print(f"-> s:{start} e:{end}, maxj:{maxj} val:{lineInt[lineIndex[maxj]]} lineIndex:{
                          lineIndex} jolt:{getWithHighlight(line, indexJoltList)}")
                    indexJoltList.append(lineIndex[maxj])
                    end = maxj
                    continue

                print(f"<- s:{start} e:{end}, maxj:{maxj} val:{lineInt[lineIndex[maxj]]} lineIndex:{
                      lineIndex} jolt:{getWithHighlight(line, indexJoltList)}")
                indexJoltList.append(lineIndex[maxj])
                start = maxj + 1

            print("jolti:", indexJoltList, "joltLen:", len(indexJoltList))

            print(getWithHighlight(line, indexJoltList))
            finalJoltString = ""
            for k in range(0, len(line.rstrip('\n'))):
                if (k in indexJoltList):
                    finalJoltString += line[k]
                    continue
            print("finalJoltString: ", finalJoltString)

        # print("\n\njolts", joltages)
        # print("sum", sum(joltages))


if __name__ == "__main__":
    main()

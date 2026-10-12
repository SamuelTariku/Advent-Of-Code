

def main():
    with open("./part1_input.txt", "r", encoding="utf8") as file:
        joltages = []
        for line in file:
            lineInt = [int(i) for i in list(line.rstrip("\n"))]

            max1i = 0
            # Find the max from the top (in case of duplicate)
            for i in range(0, len(lineInt)):
                if lineInt[i] > lineInt[max1i]:
                    max1i = i

            max2i = 0
            # If first max is at the bottom search initial list
            if max1i == (len(lineInt) - 1):
                max2i = lineInt.index(max(lineInt[:(max1i)]))
                joltages.append(int(str(lineInt[max2i])+str(lineInt[max1i])))
                continue

            # if the max is in the middle or at the rightmost
            max2i = lineInt.index(max(lineInt[max1i+1:]))
            joltages.append(int(str(lineInt[max1i])+str(lineInt[max2i])))
        print(joltages)
        print(sum(joltages))


if __name__ == "__main__":
    main()

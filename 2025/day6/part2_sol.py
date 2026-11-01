
with open("./input.txt", "r", encoding="utf8") as file:
    tabular = []
    start = True
    for line in file:
        for i in range(len(line)):
            if start:
                # print(f"|{i:<3}", end="")
                continue
        if start:
            # print()
            # print("-"*len(line)*4)
            start = False
        for i in range(len(line)):
            # print(f"|{line[i]:<3}", end="")
            try:
                tabular[i].append(line[i])
            except IndexError:
                tabular.append([line[i]])
        # print()
    # print(tabular)

    # operator is always on first column after separator (hopefully)
    opRow = True
    currentOp = "+"
    total = 0
    exp = []
    for i in range(len(tabular)):
        if opRow:
            currentOp = tabular[i].pop(-1)
        opRow = False
        sep = True
        colNum = ""
        for char in tabular[i]:
            if char != " " and char != "\n":
                sep = False
                colNum += char

        if not sep:
            exp.append(int(colNum))
            continue
        # print(f"rows: {exp} op: {currentOp}")
        if currentOp == "+":
            total += sum(exp)
        elif currentOp == "*":
            multi = 1
            for num in exp:
                multi *= num
            total += multi
        exp = []
        opRow = True
    print(total)

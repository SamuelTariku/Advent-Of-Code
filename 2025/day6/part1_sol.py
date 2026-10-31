
with open("./input.txt", "r", encoding="utf8") as file:
    tabular = []
    for f in file:
        cols = f.split()
        for i in range(len(cols)):
            try:
                tabular[i].append(cols[i])
            except IndexError:
                tabular.append([cols[i]])
    total = 0
    for rows in tabular:
        s = []
        multi = 1
        for i in range(len(rows)):
            print(rows[i], i)
            if i == (len(rows)-1):
                if rows[i] == "+":
                    total += sum(s)
                elif rows[i] == "*":
                    multi = 1
                    for j in s:
                        multi *= j
                    total += multi
                continue

            s.append(int(rows[i]))
        print(s, total, len(rows))
    print(total)

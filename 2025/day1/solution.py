
with open("input", "r") as file:
    dial = 50
    count = 0
    for line in file:
        if not line or line == "":
            continue

        in_dir = line[0].lower()
        in_num = int(line[1:])
        rot = 0

        if in_dir == "l":
            rot -= in_num
        elif in_dir == "r":
            rot += in_num
        else:
            print("err:", in_dir, "is not a valid input direction")

        dial += rot
        dial %= 100

        count += dial == 0
        print("d{:>3} -> rot{:>3}".format(dial, rot))
    print("Total Count", count)

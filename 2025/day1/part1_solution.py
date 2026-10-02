with open("input", "r") as file:
    dial = 50
    total_count = 0
    ending_count = 0
    index = 0
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

        for _ in range(in_num):
            if rot > 0:
                dial += 1
            else:
                dial -= 1
            dial %= 100
            if dial == 0:
                print("{:>3} {:>3}".format(line[:-1], total_count))
                total_count += 1

    print("Total: {}, Ending: {}".format(total_count, ending_count))

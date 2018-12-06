def create_fabric():

    full_matrix = []
    for j in range(1, 1001):
        temp_list = []
        for i in range(1, 1001):
            temp_list.append(0)
        full_matrix.append(temp_list)

    return full_matrix


def main():

    fabric_area = create_fabric()

    filename = open("../inputs/day3_input_test.txt")

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            claimID = line.split(" @ ")[0].strip("#")
            measurements = line.split("@ ")[1].split(": ")
            coords = measurements[0].split(",")
            dimensions = measurements[1].strip("\n").split("x")

            starting_x = int(coords[0])
            starting_y = int(coords[1])

            ending_x = starting_x + int(dimensions[0])
            ending_y = starting_y + int(dimensions[1])

            for i in range(starting_x, ending_x):
                for j in range(starting_y, ending_y):
                    fabric_area[j][i] = fabric_area[j][i] + 1

    # for k in fabric_area:
    #     print k

    count = 0
    for a in fabric_area:
        for b in a:
            if b > 1:
                count = count + 1
    print count


if __name__ == "__main__":
    main()
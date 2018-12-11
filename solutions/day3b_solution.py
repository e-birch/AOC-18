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
    claim_sizes = {}
    actual_claim_sizes = {}

    filename = open("../inputs/day3_input.txt")

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            claimID = line.split(" @ ")[0].strip("#")
            measurements = line.split("@ ")[1].split(": ")
            coords = measurements[0].split(",")
            dimensions = measurements[1].strip("\n").split("x")

            claim_size = int(dimensions[0]) * int(dimensions[1])
            claim_sizes[claimID] = claim_size

            starting_x = int(coords[0])
            starting_y = int(coords[1])

            ending_x = starting_x + int(dimensions[0])
            ending_y = starting_y + int(dimensions[1])

            for i in range(starting_x, ending_x):
                for j in range(starting_y, ending_y):
                    if fabric_area[j][i] == 0:
                        fabric_area[j][i] = claimID
                    else:
                        fabric_area[j][i] = "X"

    for a in fabric_area:
        for b in a:
            if b in actual_claim_sizes:
                actual_claim_sizes[b] = actual_claim_sizes[b] + 1
            else:
                actual_claim_sizes[b] = 1

    # for a in fabric_area:
    #     print a

    del actual_claim_sizes[0]
    del actual_claim_sizes["X"]

    # print len(claim_sizes)
    # print len(actual_claim_sizes)

    # print claim_sizes
    # print actual_claim_sizes

    for i in claim_sizes:
        if i in actual_claim_sizes and claim_sizes[i] == actual_claim_sizes[i]:
            print i
            break
    # count = 0
    # for a in fabric_area:
    #     for b in a:
    #         if b > 1:
    #             count = count + 1
    # print count


if __name__ == "__main__":
    main()
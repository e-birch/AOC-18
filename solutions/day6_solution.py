def count_array_values(puzzle_array):
    pre_totals_map = {}

    for i in puzzle_array:
        for j in i:
            j = j.lower()
            if j in pre_totals_map:
                pre_totals_map[j] = pre_totals_map[j] + 1
            else:
                pre_totals_map[j] = 1
    return pre_totals_map


def calculate_distances(puzzle_array, coords_map):
    for i in puzzle_array:
        for j in i:
            if j == "00":
                distances_dict = {}
                point_y = puzzle_array.index(i)
                point_x = i.index(j)

                for k in coords_map:
                    distance = abs(point_x - coords_map[k][0]) + abs(point_y - coords_map[k][1])

                    if distance in distances_dict:
                        distances_list = distances_dict[distance]
                        distances_list.append(k)
                        distances_dict[distance] = distances_list
                    else:
                        distances_dict[distance] = [k]
                if len(distances_dict[min(distances_dict)]) > 1:
                    puzzle_array[point_y][point_x] = ".."
                else:
                    puzzle_array[point_y][point_x] = distances_dict[min(distances_dict)][0].lower()
    return puzzle_array


def get_array_size(input_filename):
    filename = open(input_filename)
    max_x = 0
    max_y = 0

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            x = int(line.split(", ")[1])
            y = int(line.split(", ")[2])

            if x > max_x:
                max_x = x

            if y > max_y:
                max_y = y
    return max_x + 1, max_y + 1


def create_array(width, height):
    puzzle_array = []

    for j in range(0, height):
        x_array = []

        for i in range(0, width):
            x_array.append("00")
        puzzle_array.append(x_array)

    return puzzle_array


def plot_coords(input_filename, array):
    coords_map = {}
    filename = open(input_filename)

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            point = line.split(", ")[0]
            x = int(line.split(", ")[1])
            y = int(line.split(", ")[2])

            array[y][x] = point
            coords_map[point] = (x, y)

    return coords_map, array


def main():

    input_filename = "../inputs/day6_input_test.txt"
    array_width, array_height = get_array_size(input_filename)
    puzzle_array = create_array(array_width, array_height)

    coords_map, new_array = plot_coords(input_filename, puzzle_array)

    # for i in new_array:
    #     print i
    # print ""

    calculate_distances(new_array, coords_map)

    # for i in new_array:
    #     print i
    # print ""

    pre_totals_map = count_array_values(new_array)

    new_array[0][0] = "xx"

    new_array_height = len(new_array)
    new_array_width = len(new_array[0])

    for m in range(0, new_array_height):
        new_array[m][0] = "xx"
        new_array[m][new_array_width-1] = "xx"

    # for i in new_array:
    #     print i
    # print ""

    for n in range(0, new_array_width-1):
        new_array[0][n] = "xx"
        new_array[new_array_height-1][n] = "xx"

    # for i in new_array:
    #     print i
    # print ""

    post_totals_map = count_array_values(new_array)

    del pre_totals_map[".."]
    del post_totals_map[".."]
    del post_totals_map["xx"]

    # print pre_totals_map
    # print post_totals_map

    for i in post_totals_map:
        if post_totals_map[i] != pre_totals_map[i]:
            del pre_totals_map[i]

    print max(pre_totals_map, key=pre_totals_map.get)
    print pre_totals_map[max(pre_totals_map, key=pre_totals_map.get)]


if __name__ == "__main__":
    main()

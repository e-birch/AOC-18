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

    input_filename = "../inputs/day6_input.txt"
    array_width, array_height = get_array_size(input_filename)
    puzzle_array = create_array(array_width, array_height)

    coords_map, new_array = plot_coords(input_filename, puzzle_array)

    # for i in new_array:
    #     print i
    # print ""

    for i in new_array:
        for j in i:
            distances_dict = {}
            point_y = puzzle_array.index(i)
            point_x = i.index(j)

            total_distance = 0

            for k in coords_map:
                distance = abs(point_x - coords_map[k][0]) + abs(point_y - coords_map[k][1])
                total_distance = total_distance + distance

            new_array[point_y][point_x] = str(total_distance)

    # for i in new_array:
    #     print i
    # print ""

    for i in new_array:
        for j in i:
            point_y = puzzle_array.index(i)
            point_x = i.index(j)
            if j.isdigit():
                if int(j) >= 10000:
                    new_array[point_y][point_x] = "xx"

    # for i in new_array:
    #     print i
    # print ""

    region_size = 0

    for i in new_array:
        for j in i:
            if j != "xx":
                region_size = region_size + 1

    print region_size




if __name__ == "__main__":
    main()

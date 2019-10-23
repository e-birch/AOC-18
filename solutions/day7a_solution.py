
def read_file_into_list(input_filename):
    filename = open(input_filename)
    relations_list = []

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            line_list = line.strip("\n").split(" ")
            relations_list.append((line_list[1], line_list[7]))
    return relations_list


def get_relations_dict(line_list):

    relations_dict = {}

    for i in line_list:
        if i[0] not in relations_dict:
            relations_dict[i[0]] = []
        relations_dict[i[0]].append(i[1])

    return relations_dict


def get_all_children(relations_dict):

    all_values = relations_dict.values()
    flat_list = sum(all_values, [])

    return flat_list


def get_all_points(relations_dict):
    points_list = []

    for i in relations_dict:
        points_list.append(i)
        points_list = points_list + relations_dict[i]

    points_list = list(set(points_list))

    return points_list


def find_starting_point(points_all, points_children):
    points_order = []

    # find starting point
    for i in points_all:
        if i not in points_children:
            points_order.append(i)

    if len(points_order) > 1:
        points_order = [min(points_order)]

    return points_order


def main():

    input_filename = "../inputs/day7_input_test.txt"

    line_list = read_file_into_list(input_filename)

    relations_dict = get_relations_dict(line_list)
    points_all = get_all_points(relations_dict)
    print "All possible points are: "
    print points_all
    print "All possible children are: "
    points_children = list(set(get_all_children(relations_dict)))
    print points_children
    points_order = find_starting_point(points_all, points_children)

    print "Starting point is: "
    print points_order
    print ""

    current_children = []

    # while len(points_order) < 11:
    while len(points_order) < len(points_all):
        for i in points_order:
            if i in relations_dict:
                current_children = current_children + relations_dict[i]

        current_children = set(current_children) - set(points_order)
        current_children = list(current_children)

        children_to_remove = []
        for child in current_children:
            for j in relations_dict:
                if child in relations_dict[j] and j not in points_order:
                    children_to_remove.append(child)
                    break

        current_children = list(set(current_children) - set(children_to_remove))
        next_element = min(current_children)
        current_children.remove(next_element)
        points_order.append(next_element)

    print points_order
    # print points_all


if __name__ == "__main__":
    main()

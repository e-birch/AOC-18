import datetime
import time
import operator


def main():

    filename = open("../inputs/day4_input_sorted.txt")
    guards_dict = {}
    fmt = '%Y-%m-%d %H:%M'

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            line = line.split(" ")
            if line[2] == "Guard":
                curr_guard_id = int(line[3].strip("#"))
                if curr_guard_id not in guards_dict:
                    guards_dict[curr_guard_id] = 0
            elif line[2] == "falls":
                start_time = datetime.datetime.strptime(line[0] + " " + line[1], fmt)
            else:
                end_time = datetime.datetime.strptime(line[0] + " " + line[1], fmt)
                minutes_diff = (end_time - start_time).seconds / 60

                guards_dict[curr_guard_id] = guards_dict[curr_guard_id] + minutes_diff

    max_guard = max(guards_dict.iteritems(), key=operator.itemgetter(1))[0]
    print max_guard


if __name__ == "__main__":
    main()

import numpy as np


# Puzzle 1
def compute_vents():
    input_data = sanitize_data('input')
    points = sum(input_data, [])
    vents_map_x = max([int(point[0]) for point in points]) + 1
    vents_map_y = max([int(point[1]) for point in points]) + 1
    vents_map = np.zeros((vents_map_y, vents_map_x), dtype=np.int64)

    for line in input_data:
        # consider horizontal lines
        if line[0][1] == line[1][1]:
            mark_horizontal_line(vents_map, line)
        # consider verticle lines
        elif line[0][0] == line[1][0]:
            mark_vertical_line(vents_map, line)
        # ignore all other lines for puzzle 1
        # mark_diagonal_line for puzzle 2
        # -> for diagonal lines applies: |x1-x2|==|y1-y2|
        elif abs(int(line[0][0]) - int(line[1][0])) == abs(int(line[0][1]) - int(line[1][1])):
            mark_diagonal_line(vents_map, line)

    return compute_most_dangerous_regions(vents_map)


def compute_most_dangerous_regions(vents_map):
    return np.count_nonzero(vents_map >= 2)


def sanitize_data(file_data):
    raw_data = []
    input_data = []

    with open(file_data) as input_file:
        for line in input_file:
            raw_data.append(line.split('->'))

    for raw_line in raw_data:
        line = []
        for point in raw_line:
            line.append(point.strip().split(','))
        input_data.append(line)

    return input_data


def mark_horizontal_line(vents_map, line):
    y = int(line[0][1])

    for x in range(int(line[0][0]), int(line[1][0]) + 1):
        vents_map[y, x] += 1

    # or in case points coded the other way round
    for x in range(int(line[1][0]), int(line[0][0]) + 1):
        vents_map[y, x] += 1


def mark_vertical_line(vents_map, line):
    x = int(line[0][0])

    for y in range(int(line[0][1]), int(line[1][1]) + 1):
        vents_map[y, x] += 1

    # or in case points coded the other way round
    for y in range(int(line[1][1]), int(line[0][1]) + 1):
        vents_map[y, x] += 1


# Puzzle 2
def mark_diagonal_line(vents_map, line):
    x1 = int(line[0][0])
    y1 = int(line[0][1])
    x2 = int(line[1][0])
    y2 = int(line[1][1])
    length = abs(x1 - x2)

    if x1 <= x2 and y1 <= y2:
        for i in range(0, length + 1):
            x = x1 + i
            y = y1 + i
            vents_map[y, x] += 1

    if x1 <= x2 and y1 > y2:
        for i in range(0, length + 1):
            x = x1 + i
            y = y1 - i
            vents_map[y, x] += 1

    if x1 > x2 and y1 <= y2:
        for i in range(0, length + 1):
            x = x1 - i
            y = y1 + i
            vents_map[y, x] += 1

    if x1 > x2 and y1 > y2:
        for i in range(0, length + 1):
            x = x1 - i
            y = y1 - i
            vents_map[y, x] += 1


def main():
    print(compute_vents())


main()

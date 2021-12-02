import itertools

# Puzzle 1
def measure_depth():
    input_data = []
    #input_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    depth_increase = 0

    try:
        input_file = open("input", "r")
        input_data = input_file.readlines()
    finally:
        input_file.close()

    for i in range(1, len(input_data)):
        if int(input_data[i]) > int(input_data[i-1]):
            # print("data[i] is {} and data[i-1] is {}".format(input_data[i], input_data[i-1]))
            depth_increase = depth_increase + 1

    return depth_increase


# Puzzle 1 with itertools pairwise
def measure_depth2():
    depth_increase = 0
    with open("input") as input_file:
        for a, b in pairwise(input_file):
            if int(a) < int(b):
                depth_increase += 1

    return depth_increase



def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def triples(iterable):
    # BROKEN
    "s -> (s0,s1,s2), (s1,s2,s3), (s2, s3, s4), ..."
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    return zip(a, b, c)


# Puzzle 2
def measure_depth_3window():
    depth_increase = -1
    with open("input") as input_file:
        input_file_lines = input_file.readlines()
        previous_sum_of3 = 0
        for i in range (0, len(input_file_lines)-2):
            sum_of3 = int(input_file_lines[i]) + int(input_file_lines[i+1]) + int(input_file_lines[i+2])
            if sum_of3 > previous_sum_of3:
                depth_increase += 1
            previous_sum_of3 = sum_of3

    return depth_increase



print(measure_depth2())

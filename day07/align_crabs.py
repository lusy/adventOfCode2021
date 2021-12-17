import sys


def read_input():
    data = ""
    with open('input') as input_file:
        data = input_file.read()

    parsed_data = data.split(',')
    parsed_data_int = [int(x) for x in parsed_data]
    return parsed_data_int


# Puzzle 1
def align_crabs():
    data = read_input()
    xmin = min(data)
    xmax = max(data)
    min_fuel_spent = sys.maxsize
    #  We check all possible allignment positions x between both data points
    #  with maximum distance to each other and calculate necessary fuel to
    #  reach each of these positions, which is abs(entry - x) for entry in data
    for x in range(xmin, xmax + 1):
        fuel_spent = sum([abs(entry - x) for entry in data])
        min_fuel_spent = min(fuel_spent, min_fuel_spent)
    print(f'xmin: {xmin}')
    print(f'xmax: {xmax}')
    print(f'fuel spent: {min_fuel_spent}')


# Puzzle 2
# relatively slow, but still returns in reasonable time^^
def align_crabs_2():
    data = read_input()
    xmin = min(data)
    xmax = max(data)
    min_fuel_spent = sys.maxsize
    #  We check all possible allignment positions x between both data points
    #  with maximum distance to each other and calculate necessary fuel to
    #  reach each of these positions, which is the sum for the fuel needed at each
    #  step (which in itself always increases by 1) for abs(entry - x) steps
    for x in range(xmin, xmax + 1):
        fuel_spent = sum([sum(range(1, abs(entry - x) + 1)) for entry in data])
        min_fuel_spent = min(fuel_spent, min_fuel_spent)
    print(f'xmin: {xmin}')
    print(f'xmax: {xmax}')
    print(f'fuel spent: {min_fuel_spent}')


align_crabs_2()

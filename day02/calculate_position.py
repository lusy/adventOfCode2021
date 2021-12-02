import itertools

# Puzzle 1
def calculate_position():
    position = {
        'horizontal': 0,
        'vertical': 0
    }

    with open("input") as input_file:
        for line in input_file:
            direction, units = line.split(' ')
            if direction == 'forward':
                position['horizontal'] += int(units)
            elif direction == 'up':
                position['vertical'] -= int(units)
            elif direction == 'down':
                position['vertical'] += int(units)
            else:
                print("Unknown direction")

    return position


# Puzzle 2
def calculate_advanced_position():
    position = {
        'horizontal': 0,
        'vertical': 0,
        'aim': 0
    }

    with open("input") as input_file:
        for line in input_file:
            direction, units = line.split(' ')
            if direction == 'forward':
                position['horizontal'] += int(units)
                position['vertical'] += int(units) * position['aim']
            elif direction == 'up':
                position['aim'] -= int(units)
            elif direction == 'down':
                position['aim'] += int(units)
            else:
                print("Unknown direction")

    return position


def main():
    position = calculate_position()
    print("Puzzle1: Final position is: {} , {}".format(position['horizontal'], position['vertical']))
    multiplied = position['horizontal'] * position['vertical']
    print("Puzzle1: Position multiplied: {}".format(multiplied))

    position2 = calculate_advanced_position()
    print("Puzzle2: Final position is: horizontal: {}, vertical: {}, aim: {}".format(position2['horizontal'], position2['vertical'], position2['aim']))
    multiplied2 = position2['horizontal'] * position2['vertical']
    print("Puzzle2: Position multiplied: {}".format(multiplied2))


main()

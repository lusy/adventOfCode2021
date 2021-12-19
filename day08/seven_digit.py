def read_input():
    data = ""
    with open('input') as input_file:
        data = input_file.readlines()

    return [entry.strip() for entry in data]


# Puzzle1
def count():
    data = read_input()
    results = [entry.split(' | ')[1] for entry in data]
    results = [entry.split(' ') for entry in results]
    results_flat = sum(results, [])
    return len(list(filter(test_unique_length, results_flat)))


def test_unique_length(entry):
    if len(entry) == 2 or len(entry) == 3 or len(entry) == 4 or len(entry) == 7:
        return True
    else:
        return False


# Puzzle 2
def deduce_numbers(sequence):
    one = set(list(filter(lambda x: len(x) == 2, sequence))[0])
    #print(f'one: {one}')
    seven =  set(list(filter(lambda x: len(x) == 3, sequence))[0])
    #print(f'seven: {seven}')
    four =  set(list(filter(lambda x: len(x) == 4, sequence))[0])
    #print(f'four: {four}')
    eight =  set(list(filter(lambda x: len(x) == 7, sequence))[0])
    #print(f'eight: {eight}')
    five_segments = list(filter(lambda x: len(x)==5, sequence))
    three = set(list(filter(lambda x: one.issubset(x), five_segments))[0])
    #print(f'three: {three}')
    six_segments = list(filter(lambda x: len(x)==6, sequence))
    nine = set(list(filter(lambda x: three.issubset(x), six_segments))[0])
    #print(f'nine: {nine}')
    leftup = nine.difference(three)
    #print(f'leftup: {leftup}')
    middle = (four.difference(one)).difference(leftup)
    #print(f'middle: {middle}')
    zero = eight.difference(middle)
    #print(f'zero: {zero}')
    remaining = list(filter(lambda x: set(x) != one and set(x) != seven and set(x) != four and set(x) != eight and set(x) != three and set(x) != nine and set(x) != zero, sequence))
    six = set(list(filter(lambda x: len(x) == 6, remaining))[0])
    #print(f'six: {six}')
    five = set(list(filter(lambda x: len(x) == 5 and leftup.issubset(x), remaining))[0])
    #print(f'five: {five}')
    two = set(list(filter(lambda x: len(x) == 5 and not leftup.issubset(x), remaining))[0])
    #print(f'two: {two}')

    numbers = {
        "zero": zero,
        "one": one,
        "two": two,
        "three": three,
        "four": four,
        "five": five,
        "six": six,
        "seven": seven,
        "eight": eight,
        "nine": nine
    }
    return numbers


def compute_line(line):
    sequence_raw, results_raw = line.split(' | ')
    sequence = sequence_raw.split(' ')
    results = results_raw.split(' ')
    numbers = deduce_numbers(sequence)
    numbers_keys = list(numbers.keys())
    numbers_values = list(numbers.values())
    results_deduced = []
    for entry in results:
        position = numbers_values.index(set(entry))
        name = numbers_keys[position]
        results_deduced.append(map_numbers_to_decimal(name))

    return int(''.join(results_deduced))


def map_numbers_to_decimal(number):
    mapping =  {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    return mapping[number]


def sum_outputs():
    data = read_input()
    result = 0
    for line in data:
        result = result + compute_line(line)

    return result


def main():
    print(f'number of unique entries is {count()}')
    print(f'final sum is: {sum_outputs()}')


main()

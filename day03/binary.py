# Puzzle 1
def calculate_power_consumption():
    counter = []
    gamma_rate = []
    epsilon_rate = []

    # Initialize counters
    with open("input") as input_file:
        line = input_file.readline()
        for symbol in line.strip():
            initial = {
                'zeroes': 0,
                'ones': 0
            }
            counter.append(initial)

    with open("input") as input_file:
        for line in input_file:
            for i in range(0, len(line.strip())):
                if line[i] == '0':
                    counter[i]['zeroes'] += 1
                else:
                    counter[i]['ones'] += 1

    for elem in counter:
        if elem['zeroes'] > elem['ones'] :
            gamma_rate.append(0)
            epsilon_rate.append(1)
        else:
            gamma_rate.append(1)
            epsilon_rate.append(0)

    print("gamma rate bin: {}".format(gamma_rate))
    print("epsilon rate bin: {}".format(epsilon_rate))
    gamma_rate_decimal = calculate_decimal(gamma_rate)
    epsilon_rate_decimal = calculate_decimal(epsilon_rate)
    print("gamma rate dec: {}".format(gamma_rate_decimal))
    print("epsilon rate dec: {}".format(epsilon_rate_decimal))

    power_consumption = gamma_rate_decimal * epsilon_rate_decimal
    return power_consumption


def calculate_decimal(binary_array):
    binary_array.reverse()
    result = 1 if binary_array[0] == 1 else 0
    for i in range(1,len(binary_array)):
        result += 2 ** i * binary_array[i]

    return result


# Puzzle 2
def calculate_life_support_rating():
    input_data = []
    with open("input") as input_file:
        input_data = input_file.readlines()

    oxygen_generator_rating = calculate_rating(input_data, 'oxygen_generator')
    co2_scrubber_rating = calculate_rating(input_data, 'co2_scrubber')
    print(f'oxygen_generator rating: {oxygen_generator_rating}')
    print(f'co2 scrubber rating: {co2_scrubber_rating}')
    oxygen_generator_rating_decimal = int(oxygen_generator_rating, 2)
    co2_scrubber_rating_decimal = int(co2_scrubber_rating, 2)
    print(f'oxygen_generator rating decimal: {oxygen_generator_rating_decimal}')
    print(f'co2 scrubber rating decimal: {co2_scrubber_rating_decimal}')
    life_support_rating = oxygen_generator_rating_decimal * co2_scrubber_rating_decimal
    return life_support_rating


def calculate_rating(input_data, rating_type):
    clean_input_data = [entry.strip() for entry in input_data]
    entry_length = len(clean_input_data[0])

    for i in range(0, entry_length):
        counter = {
            'zeroes': 0,
            'ones': 0
        }

        for entry in clean_input_data:
            if entry[i] == '1':
                counter['ones'] += 1
            else:
                counter['zeroes'] += 1
        
        if (rating_type == 'oxygen_generator'):
            clean_input_data = filter_oxygen_generator(counter, clean_input_data, i)
        elif (rating_type == 'co2_scrubber'):
            clean_input_data = filter_co2_scrubber(counter, clean_input_data, i)
        else:
            print("Unknown rating type")

        if len(clean_input_data) == 1:
            return clean_input_data[0]


def filter_oxygen_generator(counter, data, position):
    if counter['ones'] >= counter['zeroes']:
        filtered_data = [entry for entry in data if entry[position] == '1']
    else:
        filtered_data = [entry for entry in data if entry[position] == '0']

    return filtered_data


def filter_co2_scrubber(counter, data, position):
    if counter['zeroes'] <= counter['ones']:
        filtered_data = [entry for entry in data if entry[position] == '0']
    else:
        filtered_data = [entry for entry in data if entry[position] == '1']

    return filtered_data


def main():
    #print(f'power consumption: {calculate_power_consumption()}')
    print(f'life support rating: {calculate_life_support_rating()}')


main()

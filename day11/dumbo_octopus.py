import numpy as np

def read_input():
    data = []
    with open('input') as input_file:
        data = input_file.readlines()

    data = [list(x.strip()) for x in data]
    data = np.array(data)
    return data.astype('int')


# Puzzle1
def model_energy_level():
    data = read_input()
    num_steps = 100
    num_flashes = 0
    increase_energy_v = np.vectorize(increase_energy)

    while num_steps > 0:
        data = increase_energy_v(data)
        while(len(data[data > 9]) > 0) :
            indexes_flashing_octopuses = np.where(data > 9)
            flashing_octopuses = data[indexes_flashing_octopuses]
            data[data > 9] = 0
            num_flashes += len(flashing_octopuses)
            increase_adjascent_energy(data, indexes_flashing_octopuses)

        num_steps -= 1

    print(f'total number of flashes: {num_flashes}')


# Puzzle 2
def compute_steps_till_all_flash():
    data = read_input()
    num_steps = 0
    increase_energy_v = np.vectorize(increase_energy)

    while len(data[data == 0]) != data.size :
        data = increase_energy_v(data)
        while(len(data[data > 9]) > 0) :
            indexes_flashing_octopuses = np.where(data > 9)
            flashing_octopuses = data[indexes_flashing_octopuses]
            data[data > 9] = 0
            increase_adjascent_energy(data, indexes_flashing_octopuses)

        num_steps += 1

    print(f'total number of steps till all octopuses flash: {num_steps}')



def increase_energy(x):
    return x + 1


def increase_adjascent_energy(data, indexes_flashing_octopuses):
    num_rows = len(data)
    num_cols = len(data[0])
    for octopus in zip(indexes_flashing_octopuses[0], indexes_flashing_octopuses[1]):
        #print(f'data: {data}')
        #print(octopus)
        if octopus[0] > 0:
            north_position = [octopus[0] - 1, octopus[1]]
            if data[north_position[0], north_position[1]] != 0:
                data[north_position[0], north_position[1]] += 1

        if octopus[0] > 0 and octopus[1] > 0:
            north_west_position = [octopus[0] - 1, octopus[1] - 1]
            if data[north_west_position[0], north_west_position[1]] != 0:
                data[north_west_position[0], north_west_position[1]] += 1

        if octopus[0] > 0 and octopus[1] < num_cols - 1:
            north_east_position = [octopus[0] - 1, octopus[1] + 1]
            if data[north_east_position[0], north_east_position[1]] != 0:
                data[north_east_position[0], north_east_position[1]] += 1

        if octopus[1] > 0:
            west_position = [octopus[0], octopus[1] - 1]
            if data[west_position[0], west_position[1]] != 0:
                data[west_position[0], west_position[1]] += 1

        if octopus[1] < num_cols - 1:
            east_position = [octopus[0], octopus[1] + 1]
            if data[east_position[0], east_position[1]] != 0:
                data[east_position[0], east_position[1]] += 1

        if octopus[0] < num_rows - 1:
            south_position = [octopus[0] + 1, octopus[1]]
            if data[south_position[0], south_position[1]] != 0:
                data[south_position[0], south_position[1]] += 1

        if octopus[0] < num_rows - 1 and octopus[1] > 0:
            south_west_position = [octopus[0] + 1, octopus[1] - 1]
            if data[south_west_position[0], south_west_position[1]] != 0:
                data[south_west_position[0], south_west_position[1]] += 1

        if octopus[0] < num_rows - 1 and octopus[1] < num_cols - 1:
            south_east_position = [octopus[0] + 1, octopus[1] + 1]
            if data[south_east_position[0], south_east_position[1]] != 0:
                data[south_east_position[0], south_east_position[1]] += 1

    #print(data)


def main():
    model_energy_level()
    compute_steps_till_all_flash()


main()

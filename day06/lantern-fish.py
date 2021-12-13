# Puzzle 1
def simulate_fish_growth():
    data = read_input()

    for counter in range(0,256):
        count_new_fish = 0
        for i, fish in enumerate(data):
            if fish == 0:
                data[i] = 6
                data.append(8)
                count_new_fish += 1
            # a newly spawned fish doesn't start counting down until next day
            elif fish == 8 and count_new_fish > 0:
                count_new_fish -= 1
                continue
            else:
                data[i] = data[i] - 1

    return data


def simulate_fish_growth_alt():
    data = read_input()
    
    for counter in range(0,256):
        birthing_fish = [6 for fish in data if fish == 0]
        rest_fish_decrease = [fish - 1 for fish in data if fish != 0]
        new_fish = [8 for fish in birthing_fish]
        data = birthing_fish + rest_fish_decrease + new_fish

    return data


def simulate_fish_growth_3():
    data = read_input()

    steps = 13
    ones = [fish for fish in data if fish == 1]
    twos = [fish for fish in data if fish == 2]
    threes = [fish for fish in data if fish == 3]
    fours = [fish for fish in data if fish == 4]
    fives = [fish for fish in data if fish == 5]

    ones_spawns = 1.ones + 2.ones + ones ( 13 - 1 = 12 = 6 * 2 )
                  |-> fangen an mit 11 steps to go und brauchen 8 down -> respawnen 1 mal, ab dann brauchen sie 6
    twos_spawns = twos + twos (13 - 2 = 11 = 6 * 1 + 5)
    threes_spawns = threes + threes ( 13 - 3 = 10 = 6 * 1 + 4)
    fours_spawns = fours + fours (13 - 4 = 9 = 6 * 1 + 3)
    fives_spawns = fives + fives (13 - 5 = 8 = 6 * 1 + 2 )






def read_input():
    data = ''
    with open('input') as input_file:
        data = input_file.read()

    data_list = data.split(',')
    data_list_ints = [int(x) for x in data_list]
    return data_list_ints


def main():
    fish_population = simulate_fish_growth_alt()
    print (len(fish_population))


main()

import numpy as np

def read_input():
    data = []
    with open('input') as input_file:
        data = input_file.readlines()

    data = [list(x.strip()) for x in data]
    return np.array(data)


# Puzzle 1
def compute_local_mins():
    data = read_input()
    num_rows = len(data)
    num_columns = len(data[0])
    local_mins = []
    local_min_positions = []
    for y in range(0, num_rows):
        for x in range(0, num_columns):
            current_point = data[y, x]
            #print(f'checking point data[{y},{x}] = {data[y,x]}')
            if y == 0 and x == 0:
                if current_point < data[y, x+1] and current_point < data[y+1, x]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])
            elif y == num_rows - 1 and x == 0:
                if current_point < data[y, x+1] and current_point < data[y-1, x]:
                    local_mins.appned(int(current_point))
                    local_min_positions.append([y,x])
            elif y == 0 and x == num_columns - 1:
                if current_point < data[y +1 , x] and current_point < data[y, x-1]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])
            elif y == 0:
                if current_point < data[y, x+1] and current_point < data[y, x-1] and current_point < data[y+1, x]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])
            elif x == 0:
                if current_point < data[y, x+1] and current_point < data[y-1, x] and current_point < data[y+1, x]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])
            elif x == num_columns -1 and y == num_rows -1:
                if current_point < data[y, x-1] and current_point < data[y-1, x]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])
            elif x == num_columns - 1:
                if current_point < data[y, x-1] and current_point < data[y-1, x] and current_point < data[y+1, x]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])
            elif y == num_rows - 1:
                if current_point < data[y, x+1] and current_point < data[y-1, x] and current_point < data[y, x -1]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])
            else:
                if current_point < data[y,x-1] and current_point < data[y, x+1] and current_point < data[y-1, x] and current_point < data[y+1, x]:
                    local_mins.append(int(current_point))
                    local_min_positions.append([y,x])

    return local_mins, local_min_positions


def compute_risk():
    local_mins, _ = compute_local_mins()
    risk = sum(local_mins) + len(local_mins)
    return risk


# Puzzle 2
def compute_biggest_basins():
    floor_map = read_input()
    _, local_min_positions = compute_local_mins()
    biggest_basins = []
    for position in local_min_positions:
        new_basin = determine_basin(floor_map, position)
        if len(biggest_basins) < 3:
            biggest_basins.append(len(new_basin))
        else:
            biggest_basins.sort()
            if len(new_basin) > biggest_basins[0]:
                biggest_basins[0]= len(new_basin)

    print(f'biggest basins: {biggest_basins}')
    print(f'biggest basins product = {biggest_basins[0] * biggest_basins[1] * biggest_basins[2]}')


def determine_basin(floor_map, position):
    basin_positions = [position]
    num_rows = len(floor_map)
    num_columns = len(floor_map[0])
    for p in basin_positions:
        if p[0] > 0:
            north_position = [p[0] - 1, p[1]]
            if floor_map[north_position[0], north_position[1]] != '9' and north_position not in basin_positions:
                basin_positions.append(north_position)
        if p[0] < num_rows - 1:
            south_position = [p[0] + 1, p[1]]
            if floor_map[south_position[0], south_position[1]] != '9' and south_position not in basin_positions:
                basin_positions.append(south_position)
        if p[1] > 0:
            west_position = [p[0], p[1] - 1]
            if floor_map[west_position[0], west_position[1]] != '9' and west_position not in basin_positions:
                basin_positions.append(west_position)
        if p[1] < num_columns - 1:
            east_position = [p[0], p[1] + 1]
            if floor_map[east_position[0], east_position[1]] != '9' and east_position not in basin_positions:
                basin_positions.append(east_position)

    return basin_positions


def main():
    #print(compute_local_mins()[1])
    compute_biggest_basins()


main()

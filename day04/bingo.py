import numpy as np

# Puzzle 1
def calculate_1st_winning_board():
    input_numbers, input_boards = sanitize_input('input_numbers', 'input_boards')

    # Play
    for number in input_numbers:
        # print(f'Number {number} is drawn!')
        for board in input_boards:
            for row in board:
                # print(f'Checking row: {row}')
                for i in range(0,len(row)):
                    if row[i] == number:
                        # print(f'It is a match!')
                        row[i] = 'x'
                if row == ['x', 'x', 'x', 'x', 'x']:
                    return win(board, int(number))
            if exists_winning_column(board):
                return win(board, int(number))


def sanitize_input(file_numbers, file_boards):
    input_numbers = []
    raw_input_boards = []
    input_boards = []

    with open(file_numbers) as input_file:
        input_numbers = input_file.read().strip().split(',')

    with open(file_boards) as input_file:
        raw_data = input_file.read().strip().split('\n\n')
        raw_input_boards = [entry.split('\n') for entry in raw_data]

    for board in raw_input_boards:
        cleaned_board = []
        for row in board:
            raw_symbols = row.strip().split(' ')
            symbols = [entry for entry in raw_symbols if entry != '']
            cleaned_board.append(symbols)
        input_boards.append(cleaned_board)

    return input_numbers, input_boards


def exists_winning_column(board):
    np_board = np.array(board)
    for i in range(0, len(board[0])):
        column = np_board[: , i]
        if np.all(column == 'x'):
            return True
    
    return False


def exists_winning_column2(board):
    return any(all(board[y][x] == 'x' for x in range(5)) for y in range(5))


def exists_winning_column3(board):
    for x in range(5):
        if all(board[y][x] == 'x' for y in range(5)):
            return True

    return False


def win(board, winning_number):
    sum_entries = 0
    for row in board:
        for entry in row:
            if entry != 'x':
                sum_entries += int(entry)

    return sum_entries * winning_number


# Puzzle 2
def calculate_last_winning_board():
    input_numbers, input_boards = sanitize_input('input_numbers', 'input_boards')
    last_winning_board = []
    winning_number = 0

    # Play
    for number in input_numbers:
        #print(f'Number {number} is drawn!')
        for j, board in enumerate(input_boards):
            if board is None:
                continue
            for row in board:
                for i in range(0,len(row)):
                    if row[i] == number:
                        row[i] = 'x'
                        if row == ['x', 'x', 'x', 'x', 'x']:
                            last_winning_board = board
                            winning_number = int(number)
                            input_boards[j] = None
                        elif exists_winning_column3(board):
                            last_winning_board = board
                            winning_number = int(number)
                            input_boards[j] = None

    return win(last_winning_board, winning_number)


def main():
    print(f'1st winning board: {calculate_1st_winning_board()}')
    print(f'last winning board: {calculate_last_winning_board()}')


main()

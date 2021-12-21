def read_data():
    data = []
    with open('input') as input_file:
        data = input_file.readlines()

    data = [entry.strip() for entry in data]
    return data


def parse_line(line):
    closing_brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    opening_brackets = closing_brackets.values()
    parsed_symbols = []
    for bracket in line:
        if bracket in opening_brackets:
            parsed_symbols.append(bracket)
        # if matching closing bracket found, remove both from parsed_symbols
        elif closing_brackets[bracket] == parsed_symbols[-1]:
            parsed_symbols.pop()
        else: # if mismatched closing bracket found, line is corrupt
            corrupted_character = bracket
            return corrupted_character

    # if no corrupted character found, the rest of the parsed symbols are the
    # ones that need closing (Puzzle2)
    return determine_completion_pattern(parsed_symbols)


def compute_scores():
    data = read_data()
    # For puzzle 1
    illegal_characters_penalty = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    syntax_error_score = 0
    autocompletion_patterns = [] # For puzzle2
    for line in data:
        parsing_result = parse_line(line)
        #print(f'parsing result: {parsing_result}')
        # For puzzle1
        if len(parsing_result) == 1:
            syntax_error_score += illegal_characters_penalty[parsing_result]
        # For puzzle2
        else:
            autocompletion_patterns.append(parsing_result)

    # For puzzle1
    print(f'syntax error score is {syntax_error_score}')

    # For puzzle2
    autocompletion_score = compute_autocompletion_score(autocompletion_patterns)
    print(f'the middle autocompletion score is {autocompletion_score}')


def compute_autocompletion_score(autocompletion_patterns):
    scores = []
    bracket_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    for pattern in autocompletion_patterns:
        pattern_score = 0
        for symbol in pattern:
            pattern_score = pattern_score * 5 + bracket_points[symbol]
        scores.append(pattern_score)

    scores.sort()
    middle_score = scores[len(scores)//2]
    #print(f'autocompletion scores: {scores}')
    return middle_score


def determine_completion_pattern(line):
    closing_brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    completion_pattern = []
    line.reverse()
    for bracket in line:
        completion_pattern.append(closing_brackets[bracket])

    return completion_pattern


def main():
    compute_scores()
    #print(parse_line('{()()()>'))


main()

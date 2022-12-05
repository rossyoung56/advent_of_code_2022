shape_points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
outcome_points = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6,
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0,
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3,
    },
}

with open('../resources/day2_input.txt', 'r') as in_file:
    points = 0

    for line in in_file:
        shapes = line.strip().split(' ')
        opponent = shapes[0]
        self = shapes[1]

        points += shape_points[self]
        points += outcome_points[self][opponent]

    print(f'Points: {points}')

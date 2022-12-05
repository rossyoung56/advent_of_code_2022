shape_points = {
    'A': 1,
    'B': 2,
    'C': 3,
}
outcome_points = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}
decisions = {
    'X': {
        'A': 'C',
        'B': 'A',
        'C': 'B',
    },
    'Y': {
        'A': 'A',
        'B': 'B',
        'C': 'C',
    },
    'Z': {
        'A': 'B',
        'B': 'C',
        'C': 'A',
    },
}

with open('../resources/day2_input.txt', 'r') as in_file:
    points = 0

    for line in in_file:
        shapes = line.strip().split(' ')
        opponent = shapes[0]
        self_outcome = shapes[1]
        self_decision = decisions[self_outcome][opponent]

        points += shape_points[self_decision]
        points += outcome_points[self_outcome]

    print(f'Points: {points}')

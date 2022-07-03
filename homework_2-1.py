from itertools import permutations


def create_path():
    return [[None, [], None], []]


def add_first_point(path: list, point: tuple) -> None:
    path[0][0] = point


def add_last_point(path: list, point: tuple) -> None:
    path[0][2] = point


def add_middle_point(path: list, point: tuple) -> None:
    path[0][1].append(point)


def get_length_between_two_points(point_a: tuple, point_b: tuple) -> float:
    return ((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5


def get_length_between_all_points(path: list):
    n = len(path[0][1]) + 1
    for i in range(n):
        if i == 0:
            length_path = get_length_between_two_points(path[0][0], path[0][1][i])
            path[1].append(length_path)
        elif i < len(path[0][1]):
            length_path = get_length_between_two_points(path[0][1][i-1], path[0][1][i])
            path[1].append(length_path + path[1][i-1])
        else:
            length_path = get_length_between_two_points(path[0][1][i-1], path[0][2])
            path[1].append(length_path + path[1][i-1])


def get_combinations(path):
    combination_list = []
    for i in permutations(path[0][1]):
        temp_path = create_path()
        temp_path[0][0] = path[0][0]
        temp_path[0][2] = path[0][2]
        temp_path[0][1] = list(i)
        combination_list.append(temp_path)
    return combination_list


def calculate_min_path(path: list):
    if len(path[0][1]) == 0:
        length_path = get_length_between_two_points(path[0][0], path[0][2])
        path[1].append(length_path)
        return path
    elif len(path[0][1]) == 1:
        get_length_between_all_points(path)
        return path
    else:
        min_path = None
        combination_list = get_combinations(path)
        for i in combination_list:
            get_length_between_all_points(i)
            if min_path is None:
                min_path = i
            elif min_path[1][-1:] > i[1][-1:]:
                min_path = i
        return min_path


def display_path(path):
    n = len(path[0][1]) + 1
    for i in range(n):
        if i == 0:
            print(f'{path[0][0]} -> {path[0][1][i]}[{path[1][i]}] -> ', end=' ')
        elif i < len(path[0][1]):
            print(f'{path[0][1][i]}[{path[1][i]}] -> ', end=' ')
        else:
            print(f'{path[0][2]}[{path[1][i]}] = {path[1][i]}')


if __name__ == "__main__":
    path_1 = create_path()
    add_first_point(path_1, (0, 2))
    add_last_point(path_1, (0, 2))
    add_middle_point(path_1, (2, 5))
    add_middle_point(path_1, (5, 2))
    add_middle_point(path_1, (6, 6))
    add_middle_point(path_1, (8, 3))

    path_finish = calculate_min_path(path_1)
    display_path(path_finish)



























import math
from datetime import timedelta


def calculate_square_root(x):
    assert x >= 0, "Input must be non-negative"
    return math.sqrt(x)


def find_max(array: list[int]):
    # Ak je list prazdny, vyhodi AssertionError
    assert array
    highest = array[0]
    for elem in array:
        if elem > highest:
            highest = elem

    return highest


def add_times(time, time_shift):
    # Special logic, has to be at least 2 days
    assert time_shift >= timedelta(
        days=2
    ), "Cannot add less than 2 days"
    return time + time_shift


def foo(data, replace=False):
    assert replace or isinstance(
        data, list
    ), "Data must be list if replace is False"
    return ...

# V testoch sa potom pouziva obdoba assertu pre testovanie rovnosti objektov,
# ci padla funkcia na chybe ako mala a podobne.
# Napriklad
# self.assertEqual(response.status_code, 404)

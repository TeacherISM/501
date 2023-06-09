"""

Module that sums two integer numbers.

Author: Francisco D. Salcedo

"""


def number_sum(number_one, number_two):
    """

    Function that sums two numbers if they are integers.

    """
    if isinstance(number_one, int) and isinstance(number_two, int):
        return number_one + number_two
    return None

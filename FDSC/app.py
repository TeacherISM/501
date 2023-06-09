"""

Module that sums two integer numbers.

Author: Francisco D. Salcedo

"""


def lambda_handler(event, context):
    """
    Code for a lambda aws handler to sum two numbers.
    """

    print(context)

    number_one = event['number_one']
    number_two = event['number_two']

    if isinstance(number_one, int) and isinstance(number_two, int):
        return number_one + number_two
    return None

def sum_numbers(a, b):
    return a + b


def lambda_handler(event, context):
    num1 = event.get('num1')
    num2 = event.get('num2')

    result = sum_numbers(num1, num2)
    print(f"Sum: {result}")

    return result

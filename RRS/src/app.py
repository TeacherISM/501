def sum_numbers(x, y):
    return x + y

def lambda_handler(event, context):
    result = sum_numbers(event['x'], event['y'])
    return result
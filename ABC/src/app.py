import json


def lambda_handler(event, context):
    # Extract the numbers from the event payload
    number1 = event['number1']
    number2 = event['number2']

    # Perform the addition
    result = number1 + number2

    # Prepare the response
    response = {
        'statusCode': 200,
        'body': json.dumps({'sum': result})
    }

    return response

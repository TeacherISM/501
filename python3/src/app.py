import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ...
    result = None
    action = event.get('action')
    if action == 'increment':
        result = event.get('number', 0) + 1
        logger.info('Calculated result of %s', result)
    else:
        logger.error("%s is not a valid action.", action)

    response = {'result': result}
    return response
{
    "action": "increment",
    "number": 3
}

def lambda_handler(event, context):
    # Get the numbers from the event payload
    numbers = event['numbers']
    
    # Sum up the numbers
    total = sum(numbers)
    
    # Return the result
    return {
        'statusCode': 200,
        'body': total
    }

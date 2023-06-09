

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

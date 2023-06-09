def lambda_handler(event, context):
    n1 = 11
    n2 = 7

    sum = n1+n2
    return {
        'statusCode': 200,
        'body': n1 + n2 
    }

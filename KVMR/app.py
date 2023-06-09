def handler(event, context):
    return {
        'statusCode': 200,
        'body': str(50 + 5.5)
    }

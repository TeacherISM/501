import logging
def aws_Lambda(event, context):
    a = 1
    b = 2
    logging.info(a + b)
    return {
        'statusCode': 200,
        'body': a + b}
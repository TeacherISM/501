import os

def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    num1 = 13
    num2 = 77
    suma = num1 + num2
    return suma
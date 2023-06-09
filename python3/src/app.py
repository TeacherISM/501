"""  
import os
import json 

def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    json_suma = lambda a,b :  a+b
    return  json_suma
"""
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
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
import os
import json


def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    return 2 + 2

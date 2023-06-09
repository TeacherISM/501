def lambda_handler(event, context):
    num1 = event['num1']
    num2 = event['num2']
    sum = num1 + num2
    print("La suma es: ", sum)
    return {
        'statusCode': 200,
        'body': sum
    }

def AWS_Lambda(event, context):
    a = 1
    b = 2
    
    print(a+b)
    return {
        'statusCode': 200,
        'body': a + b
    }
    
    

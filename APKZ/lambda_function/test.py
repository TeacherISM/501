from sumLambda import lambda_handler

def test_lambda_handler():
    event = {
        'num1': 3,
        'num2': 5
    }
    context = {} 
    result = lambda_handler(event, context)
    assert result['statusCode'] == 200
    assert result['body'] == 8

def test_lambda_handler_negative_numbers():
    event = {
        'num1': -3,
        'num2': -5
    }
    context = {} 
    result = lambda_handler(event, context)
    assert result['statusCode'] == 200
    assert result['body'] == -8

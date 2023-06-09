import app


def test_handler():
    event = {}
    context = {}
    response = app.handler(event, context)

    print("Status Code:", response['statusCode'])
    print("Body:", response['body'])

    assert response['statusCode'] == 200
    assert response['body'] == '55.5'
